import asyncio
import time

async def fetch_data(task_id, delay):
    print(f"  [요청] Task {task_id} (대기: {delay}초 시작)")
    await asyncio.sleep(delay) # 제어권을 양보하며 논블로킹 대기
    print(f"  [완료] Task {task_id}")
    return f"Data_{task_id}"

async def main():
    # 🔴 패턴 1. 순차 실행 (동기 프로그램과 동일한 동작)
    print("\n--- 1. 순차 실행 (Sequential) ---")
    start = time.time()
    res1 = await fetch_data(1, 2) # 완전히 끝날 때까지 2초 대기
    res2 = await fetch_data(2, 1) # 그 후 1초 대기
    print(f"소요 시간: {time.time() - start:.2f}초") # 총 3초 소요

    # 🟡 패턴 2. 동시 실행 (create_task 사용)
    print("\n--- 2. 동시 실행 (Concurrent with create_task) ---")
    start = time.time()
    # Task 생성 즉시 백그라운드에서 타이머가 동시에 돌아가기 시작함
    task1 = asyncio.create_task(fetch_data(3, 2))  
    task2 = asyncio.create_task(fetch_data(4, 1))  
    
    res3 = await task1
    res4 = await task2
    print(f"소요 시간: {time.time() - start:.2f}초") # 가장 긴 대기 시간인 총 2초 소요

    # 🟢 패턴 3. 동시 실행 (gather 사용 - 실무에서 가장 많이 쓰임)
    print("\n--- 3. 동시 실행 (Concurrent with gather) ---")
    start = time.time()
    results = await asyncio.gather(
        fetch_data(5, 2), 
        fetch_data(6, 1)
    )
    print(f"최종 결과: {results} / 소요 시간: {time.time() - start:.2f}초") # 총 2초 소요

if __name__ == "__main__":
    asyncio.run(main())