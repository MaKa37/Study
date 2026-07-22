"""
샘플 학습 코드
아래 코드는 기준 경로를 잡고 -> 폴더를 생성하고 -> 파일을 쓴 뒤 -> 전체 폴더를 뒤져서 파일 정보를 추출하는 실무 데이터 수집/처리 스크립트의 전형적인 패턴입니다.
"""
import os, stat, shutil
from pathlib import Path

# ==========================================
# [실무 유틸리티] 삭제 실패 시 권한을 변경하고 재시도하는 콜백 함수
# ==========================================
def handle_remove_readonly(func, path, exc_info):
    """
    Windows 환경 등에서 파일이 '읽기 전용' 상태이거나 권한이 꼬여
    shutil.rmtree가 실패할 때 호출됩니다.
    쓰기 권한을 강제로 부여한 뒤 삭제를 재시도합니다.
    """
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as e:
        print(f"[경고] 권한 변경 후 삭제 실패 ({path}): {e}")

# 1. 동적 기준 경로 및 객체지향 경로 결합 (슬래시 연산자)
# 실무에서는 현재 스크립트 위치를 기준으로 삼는 경우가 많습니다.
# base_dir = Path(__file__).resolve().parent
base_dir = Path.cwd() / "project_work_space" # 학습을 위해 현재 실행 위치 기준 적용
data_dir = base_dir / "data" / "json_files"

# 2. 안전한 디렉터리 생성 (중간 폴더 project_workspace/data 까지 한 번에 생성)
data_dir.mkdir(parents=True, exist_ok=True)
print(f"[알림] 작업 디렉터리 준비 완료: {data_dir}")

# 3. 편의 기능 I/O를 활용한 더미 파일 생성
# with open() 구문 없이 단 한 줄로 파일을 생성하고 내용을 씁니다.
file_1 = data_dir / "dataset_A.json"
file_2 = data_dir / "dataset_B.json"

file_1.write_text('{"id": 1, "status": "success"}', encoding="utf-8")
file_2.write_text('{"id": 2, "status": "pending"}', encoding="utf-8")

# 4. 검증 및 판별
if data_dir.exists():
    print("\n[알림] 데이터 폴더가 정상적으로 존재합니다. 파일 탐색을 시작합니다.")

# 5. 고급 파일 탐색 (rglob) 및 경로 속성 추출
# base_dir 아래에 있는 모든 .json 파일을 찾아 정보를 파싱합니다.
print("-" * 40)
for file_path in base_dir.rglob("*.json"):
    print(f"전체 경로 : {file_path}")
    print(f"상위 폴더 : {file_path.parent}")
    print(f"파일 이름 : {file_path.name}")
    print(f"확 장 자  : {file_path.suffix}")

    # 간편한 읽기 테스트
    content = file_path.read_text(encoding="utf-8")
    print(f"파일 내용 : {content}\n")

# ==========================================
# 6. 파일/폴더 안전 삭제 로직
# ==========================================
print("-" * 40)
print("[알림] 안전 삭제 프로세스를 시작합니다.")

if base_dir.exists():
    try:
        # Path 객체를 직접 전달합니다.
        # Python 3.12 미만 버전에서는 onerror=handle_remove_readonly 사용
        # Python 3.12 이상 버전에서는 onexc=handle_remove_readonly 사용 권장
        shutil.rmtree(base_dir, onerror=handle_remove_readonly)
        print(f"[성공] 임시 작업 디렉터리 '{base_dir.name}' 및 하위 파일 전체 삭제 완료.")

    except Exception as e:
        # 다른 프로그램(백신, IDE 등)이 파일을 꽉 잡고 있어(점유 상태) 지울 수 없는 등
        # 치명적인 문제가 발생했을 때 프로그램이 뻗지 않도록 로깅 후 남깁니다.
        print(f"[크리티컬 에러] 디렉터리 삭제 실패. 수동 확인이 필요합니다.\n원인: {e}")

else:
    print("[알림] 삭제할 대상 디렉터리가 이미 존재하지 않습니다.")