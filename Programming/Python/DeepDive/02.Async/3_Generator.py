import asyncio

async def async_data_stream():
    """0.5초마다 데이터를 하나씩 스트리밍하는 비동기 제너레이터"""
    for i in range(1, 4):
        await asyncio.sleep(0.5) # 네트워크 대기 시뮬레이션
        yield f"Data Chunk {i}"

async def process_stream():
    print("--- 비동기 스트리밍 수신 시작 ---")
	# 비동기 반복자(async for)를 사용하여 값을 순차적으로 꺼냄
    async for chunk in async_data_stream():
        print(f"수신 처리 완료: {chunk}")
        
if __name__ == "__main__":
    asyncio.run(process_stream())