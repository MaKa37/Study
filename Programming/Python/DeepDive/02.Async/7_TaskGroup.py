import asyncio

async def controlled_task(id, delay, fail=False):
    try:
        await asyncio.sleep(delay)
        if fail:
            print(f"[Task {id}] 예외 발생 준비!")
            raise ValueError(f"Task {id} 치명적 오류!")

    except asyncio.CancelledError:
        # 다른 태스크가 실패하여 TaskGroup에 의해 강제 취소될 때 호출됨
        print(f"[Task {id}] 다른 작업의 실패로 인해 강제 취소되었습니다.")
        raise

async def modern_task_group():
    try:
        # async with 블록을 빠져나올 때 내부의 모든 태스크가 완료되기를 자동으로 대기합니다.
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(controlled_task(1, 3)) # 3초가 필요한 정상 작업
            task2 = tg.create_task(controlled_task(2, 1, fail=True)) # 1초 만에 실패하는 작업

    except* ValueError as e:  # ExceptionGroup 처리를 위한 새로운 except* 구문 (Python 3.11+)
        print(f"\n태스크 그룹 내에서 에러가 발생했습니다: {e.exceptions}")
        print("-> task2가 실패하는 즉시, 3초를 기다리던 task1은 1초 시점에 바로 취소(Cancel)되어 리소스를 아낍니다.")

if __name__ == "__main__":
    asyncio.run(modern_task_group())