## SQL SCHEMA AND TABLE

```sql
-- 1. 전용 스키마 생성
CREATE SCHEMA IF NOT EXISTS macro_econ;

-- 2. 한국은행 기준금리 테이블 생성
CREATE TABLE IF NOT EXISTS macro_econ.bok_base_rate (
    base_date       DATE           NOT NULL, -- 기준 일자 (YYYY-MM-DD)
    stat_code       VARCHAR(20)    NOT NULL, -- 통계표 코드 (예: 722Y001)
    stat_name       VARCHAR(100)   NOT NULL, -- 통계표 명칭
    item_code       VARCHAR(20)    NOT NULL, -- 통계 항목 코드 (예: 0101000)
    item_name       VARCHAR(100)   NOT NULL, -- 통계 항목 명칭
    base_rate       NUMERIC(5, 2)  NOT NULL, -- 기준금리 (%)
    unit_name       VARCHAR(20)    NOT NULL DEFAULT '%', -- 단위
    created_at      TIMESTAMPTZ    NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 최초 수집시각
    updated_at      TIMESTAMPTZ    NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 최종 수정시각
    CONSTRAINT pk_bok_base_rate PRIMARY KEY (base_date, stat_code, item_code)
);

-- 3. 조회 성능 최적화를 위한 인덱스 생성 (시계열 범위 조회용)
CREATE INDEX IF NOT EXISTS idx_bok_base_rate_date 
    ON macro_econ.bok_base_rate (base_date DESC);

-- 4. updated_at 자동 갱신을 위한 PL/pgSQL 트리거 함수 정의
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 5. 트리거 바인딩
DROP TRIGGER IF EXISTS trigger_update_bok_base_rate_updated_at ON macro_econ.bok_base_rate;
CREATE TRIGGER trigger_update_bok_base_rate_updated_at
    BEFORE UPDATE ON macro_econ.bok_base_rate
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```