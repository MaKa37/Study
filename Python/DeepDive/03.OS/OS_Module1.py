import os

def find_large_files(target_dir, min_mb=100):
    # MB 단위 변환을 위한 바이트 기준값
    BYTES_IN_MB = 1024 * 1024
    min_bytes = min_mb * BYTES_IN_MB

    print(f"🔍 '{target_dir}' 경로에서 {min_mb}MB 이상의 파일을 탐색합니다...\n")

    # os.walk를 통한 하위 디렉터리 전체 순회
    for root_path, dirs, files in os.walk(target_dir):
        for file_name in files:
            # 파일의 전체 절대 경로 조립 (os.path.join 활용)
            full_path = os.path.join(root_path, file_name)

            try:
                # 파일 메타데이터(상태) 취득
                file_size = os.stat(full_path).st_size

                # 조건 검사: 지정한 용량 이상인지 확인
                if file_size >= min_bytes:
                    size_in_mb = file_size / BYTES_IN_MB
                    print(f"[대용량 발견] {size_in_mb:.2f} MB | {full_path}")

            except FileNotFoundError:
                # 탐색 중 파일이 삭제되거나 권한이 없는 경우 예외 처리
                print(f"[접근 불가] {full_path}")

            else:
                print(f"{file_name} -> Check Complete")

# 현재 디렉터리(.)를 기준으로 탐색 실행 (실제 사용시 경로 변경 가능)
find_large_files(".", min_mb=100)