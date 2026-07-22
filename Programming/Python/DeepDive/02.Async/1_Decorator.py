import asyncio, time, functools

def async_timer(func):
    """비동기 함수의 실행 시간을 측정하는 데코레이터"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs) # 비동기 원본 함수 대기
        end_time = time.time()
        print(f"[{func.__name__}] 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

@async_timer
async def fetch_mock_data():
    print("데이터 로딩 중...")
    await asyncio.sleep(1)  # 1초간 I/O 대기 시뮬레이션
    return "데이터 로드 완료"

if __name__ == "__main__":
    asyncio.run(fetch_mock_data())

"""
이 코드에서의 전체 흐름
1. fetch_mock_data()가 호출되면 데코레이터 내부의 wrapper(*args, kwargs)가 먼저 실행됩니다.

2. start_time = time.time()으로 시작 시간을 기록합니다.

3. await func(*args, kwargs)를 통해 실제 fetch_mock_data()의 내용(데이터 로딩 중... 및 1초 대기)을 실행합니다.

4. 실행이 끝나면 end_time = time.time()으로 종료 시간을 기록하고 그 차이를 출력합니다.
"""