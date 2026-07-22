import os
import shutil

# 1. 환경 변수 조회 (API 키, 설정값 등 안전하게 불러오기)
# 설정된 값이 없으면 'default_key'를 반환합니다.
api_key = os.environ.get('MY_API_KEY', 'default_key')
print(f"1. 설정된 API KEY: {api_key}")

# 2. 다중 디렉터리 생성 (결과물을 저장할 폴더 구조 한 번에 생성)
# exist_ok=True 옵션을 주면 이미 폴더가 있어도 에러가 발생하지 않습니다.
work_dir = "./project/python"
os.makedirs(work_dir, exist_ok=True)
print(f"2. 디렉터리 생성 완료: {work_dir}")

# (테스트를 위한 더미 파일 생성)
target_file = f"{work_dir}/app_log.txt"
with open(target_file, 'w') as f:
    f.write("에러 로그 데이터...")

# 3. 파일 복사 (중요한 데이터를 백업 폴더로 복사)
backup_dir = "./project/backup"
os.makedirs(backup_dir, exist_ok=True)
shutil.copy(target_file, backup_dir)
print(f"3. 파일 복사 완료: {target_file} -> {backup_dir}")

# 4. 단일 디렉터리 조회 (백업이 잘 되었는지 폴더 내부 확인)
backup_files = os.listdir(backup_dir)
print(f"4. 백업 폴더 내 파일 목록: {backup_files}")

# 5. 내용물 있는 폴더 전체 삭제 (작업 완료 후 임시 폴더 일괄 정리)
# project_data 폴더와 그 안의 logs, backup 폴더, 파일들이 모두 삭제됩니다.
shutil.rmtree("./project")
print("5. 임시 디렉터리 일괄 정리(삭제) 완료")