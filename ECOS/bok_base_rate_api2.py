import os
import sys
import logging
from datetime import datetime, timezone
from typing import Dict, List, Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

# =====================================================================
# 1. 로깅 및 환경 변수 설정
# =====================================================================
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

load_dotenv()

class Config:
    """애플리케이션 설정 및 환경변수 관리"""
    BOK_API_KEY: str = os.getenv("BOK_API_KEY", "")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "postgres")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    
    @classmethod
    def get_db_url(cls) -> str:
        return f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"

    @classmethod
    def validate(cls):
        if not cls.BOK_API_KEY:
            raise ValueError("환경변수에 BOK_API_KEY가 설정되지 않았습니다.")


# =====================================================================
# 2. 한국은행 ECOS API Client
# =====================================================================
class BokApiClient:
    """한국은행 Open API 통신 클라이언트"""
    BASE_URL = "http://ecos.bok.or.kr/api/StatisticSearch"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = self._create_retry_session()

    def _create_retry_session(self) -> requests.Session:
        """네트워크 지연 및 순간 오류에 대응하는 Retry Session 생성"""
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,  # 1초, 2초, 4초 간격 재시도
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def fetch_base_rate(
        self, 
        start_date: str, 
        end_date: str, 
        stat_code: str = "722Y001", 
        item_code: str = "0101000",
        cycle: str = "D"
    ) -> List[Dict[str, Any]]:
        raw_items: List[Dict[str, Any]] = []
        start_idx = 1
        page_size = 1000

        while True:
            end_idx = start_idx + page_size - 1
            url = f"{self.BASE_URL}/{self.api_key}/json/kr/{start_idx}/{end_idx}/{stat_code}/{cycle}/{start_date}/{end_date}/{item_code}"
            
            logger.info(f"API 요청 중: {start_idx} ~ {end_idx} 번 건")
            
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                if "StatisticSearch" not in data:
                    if "RESULT" in data:
                        logger.warning(f"API 호출 결과 메시지: {data['RESULT']['MESSAGE']}")
                    break

                search_result = data["StatisticSearch"]
                rows = search_result.get("row", [])
                raw_items.extend(rows)

                total_count = int(search_result.get("list_total_count", 0))
                if end_idx >= total_count:
                    break

                start_idx += page_size

            except requests.exceptions.RequestException as e:
                logger.error(f"HTTP 요청 실패: {e}")
                raise
            except Exception as e:
                logger.error(f"응답 데이터 파싱 중 오류 발생: {e}")
                raise

        logger.info(f"총 {len(raw_items)}건의 데이터를 성공적으로 수신했습니다.")
        return raw_items


# =====================================================================
# 3. 데이터 변환 및 전처리 (Data ETL Transformation)
# =====================================================================
class DataTransformer:
    """수신된 API 데이터 정제 및 DB 포맷 변환 클래스"""
    
    @staticmethod
    def transform_base_rate(raw_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        transformed = []
        for item in raw_items:
            try:
                time_str = item["TIME"]
                if len(time_str) == 8:
                    base_date = datetime.strptime(time_str, "%Y%m%d").date()
                elif len(time_str) == 6:
                    base_date = datetime.strptime(time_str, "%Y%m").date()
                else:
                    logger.warning(f"지원하지 않는 날짜 포맷 스킵: {time_str}")
                    continue

                # 결측치(빈 문자열) 방어 로직 추가
                data_value_str = str(item.get("DATA_VALUE", "")).strip()
                if not data_value_str:
                    continue  

                transformed.append({
                    "base_date": base_date,
                    "stat_code": item["STAT_CODE"],
                    "stat_name": item["STAT_NAME"],
                    "item_code": item["ITEM_CODE1"],
                    "item_name": item["ITEM_NAME1"],
                    "base_rate": float(data_value_str),
                    "unit_name": item.get("UNIT_NAME", "%")
                })
            except (ValueError, KeyError) as e:
                logger.error(f"데이터 변환 실패 행 스킵 - Raw Data: {item}, Error: {e}")
                continue

        return transformed


# =====================================================================
# 4. PostgreSQL 데이터베이스 저장 파이프라인 (UPSERT)
# =====================================================================
class PostgresPipeline:
    """PostgreSQL 연결 및 멱등적(Idempotent) 데이터 저장 관리"""

    def __init__(self, db_url: str):
        self.engine: Engine = create_engine(
            db_url,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True
        )
        self.metadata = MetaData(schema="macro_econ")
        self.table = self._reflect_table()

    def _reflect_table(self) -> Table:
        """PostgreSQL에 생성된 테이블 스키마를 동적으로 읽어옴 (Auto Reflection)"""
        return Table("bok_base_rate", self.metadata, autoload_with=self.engine)

    def upsert_records(self, records: List[Dict[str, Any]]) -> int:
        if not records:
            logger.info("저장할 데이터가 없습니다.")
            return 0

        stmt = insert(self.table).values(records)

        # DB단 트리거(BEFORE UPDATE)가 updated_at을 관리하므로 제외
        update_cols = {
            "stat_name": stmt.excluded.stat_name,
            "item_name": stmt.excluded.item_name,
            "base_rate": stmt.excluded.base_rate,
            "unit_name": stmt.excluded.unit_name
        }

        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=["base_date", "stat_code", "item_code"],
            set_=update_cols
        )

        try:
            with self.engine.begin() as conn:
                result = conn.execute(upsert_stmt)
                logger.info(f"성공적으로 {len(records)}건의 데이터를 DB에 반영(Upsert)했습니다.")
                return result.rowcount
        except SQLAlchemyError as e:
            logger.error(f"데이터베이스 적재 트랜잭션 오류: {e}")
            raise


# =====================================================================
# 5. 메인 실행 제어
# =====================================================================
def main():
    Config.validate()

    api_client = BokApiClient(api_key=Config.BOK_API_KEY)
    
    start_date = "20000101"
    end_date = datetime.today().strftime("%Y%m%d")

    logger.info(f"기준금리 수집 시작 (기간: {start_date} ~ {end_date})")

    raw_data = api_client.fetch_base_rate(
        start_date=start_date,
        end_date=end_date,
        stat_code="722Y001",  
        item_code="0101000",  
        cycle="D"             
    )

    if not raw_data:
        logger.warning("조회된 데이터가 없습니다. 파이프라인을 종료합니다.")
        return

    transformed_data = DataTransformer.transform_base_rate(raw_data)

    db_pipeline = PostgresPipeline(db_url=Config.get_db_url())
    db_pipeline.upsert_records(transformed_data)


if __name__ == "__main__":
    main()