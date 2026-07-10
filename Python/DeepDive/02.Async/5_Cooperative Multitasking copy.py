import asyncio

# 3.2 코루틴: 중간에 멈출 수 있는 함수
async def bake_bread():
    print("빵 굽기 시작...")
    await asyncio.sleep(1) # 오븐에 넣고 다른 작업을 할 수 있게 제어권 반환
    return "빵 완성"

async def main():
    # 3.3 태스크: 이벤트 루프에 코루틴 예약 및 백그라운드 실행
    task = asyncio.create_task(bake_bread())
    
	# 3.4 퓨처: 완료될 때까지 대기 후 결과(상태) 반환
    result = await task
    print(result)

 # 3.1 이벤트 루프: 루프를 생성하고 메인 진입점을 실행
asyncio.run(main())
