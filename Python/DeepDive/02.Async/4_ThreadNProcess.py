import asyncio, time
from concurrent.futures import ProcessPoolExecutor

def heavy_cpu_task(name):
	"""이벤트 루프를 멈추게 할 수 있는 무거운 동기 연산"""
	print(f"[{name}] 무거운 연산 시작 (다른 코어에서 실행 중)")
	result = sum(i * i for i in range(10**7))
	return result

async def main():
	loop = asyncio.get_running_loop()

	# 무거운 CPU 연산을 완전히 독립된 프로세스 풀로 던집니다.
	with ProcessPoolExecutor() as pool:
		# run_in_executor는 논블로킹으로 작동하여 퓨처(Future)를 반환합니다.
		future = loop.run_in_executor(pool, heavy_cpu_task, "AI 데이터 전처리")

		print("메인 루프: 연산이 진행되는 동안 저는 다른 비동기 작업을 처리합니다!")
		await asyncio.sleep(1) 

		result = await future # 연산이 끝날 때까지 대기 후 결과 수신
		print(f"연산 완료: {result}")
		
if __name__ == "__main__":
	asyncio.run(main())
	
