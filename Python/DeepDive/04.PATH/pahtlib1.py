"""
프로그램을 터미널의 어느 위치에서 실행하든 상관없이, 항상 스크립트 파일과 같은 폴더에 있는 설정 파일(`config.json`)을 안전하게 읽어오는 함수를 작성합니다.
"""

import json
from pathlib import Path

def load_config(file_name="config.json"):
    # 1. 현재 실행 중인 스크립트 파일의 절대 경로를 구하고, 그 부모 폴더를 찾음
    # __file__ 은 현재 파이썬 파일의 위치를 나타내는 특수 변수입니다.
    current_dir = Path(__file__).resolve().parent

    # 2. 슬래시(/) 연산자를 이용해 대상 파일의 완벽한 절대 경로 조립
    config_path = current_dir / file_name

    print(f"🔍 로드 시도 경로: {config_path}")

    # 3. 경로 유효성 검증 및 파일 읽기
    if config_path.exists() and config_path.is_file():
        # Path.read_text()로 간편하게 텍스트를 읽어와 JSON으로 파싱
        data = json.loads(config_path.read_text(encoding='utf-8'))
        print("✅ 설정 파일 로드 성공!")
        return data
    else:
        print("❌ 설정 파일을 찾을 수 없습니다.")
        return None
    
# 함수 실행 테스트
my_config = load_config()