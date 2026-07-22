"""
[코드 실습] 파일 이관 및 경로 유효성 사전 검증 시스템

원본 경로(`src`)에서 목적지 경로(`dst`)로 파일을 복사할 때, 원본이 실제로 존재하는지 꼼꼼하게 사전 체크하고, 목적지 폴더가 없다면 에러 없이 중간 폴더까지 자동 생성하여 복사하는 방어적 프로그램을 작성합니다.
"""

import shutil
from pathlib import Path

def safe_copy_file(src_path_str, dst_dir_str):
    # 1. 입력받은 문자열을 Path 객체로 변환
    src_file = Path(src_path_str)
    dst_dir = Path(dst_dir_str)
    
    # 2. 원본 경로 유효성 사전 검증 (방어적 프로그래밍)
    if not src_file.exists():
        print(f"🚨 오류: 원본을 찾을 수 없습니다 -> {src_file}")
        return
    if not src_file.is_file():
        print(f"🚨 오류: 대상이 파일이 아닙니다(폴더일 수 있음) -> {src_file}")
        return
        
    # 3. 목적지 폴더가 없다면 상위 폴더(parents) 포함하여 에러 없이 생성
    dst_dir.mkdir(parents=True, exist_ok=True)
    
    # 4. 목적지 파일 객체 조립 (폴더 경로 / 원본 파일명)
    target_file = dst_dir / src_file.name
    
    # 5. 파일 복사 수행 (shutil.copy는 Path 객체도 잘 지원합니다)
    shutil.copy(src_file, target_file)
    print(f"📦 복사 완료: {src_file.name}")
    print(f"   -> 저장 위치: {target_file}")


# 실행 예시 
safe_copy_file("data/raw_data.csv", "backup/2026/01")