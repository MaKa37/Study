import asyncio

class AsyncNumberIterator:
	"""지정된 범위까지 비동기적으로 숫자를 생성하는 사용자 정의 비동기 이터레이터"""
	def __init__(self, stop):
		self.current = 0
		self.stop = stop

	def __aiter__(self):
		return self

	async def __anext__(self):
		if self.current < self.stop:
			await asyncio.sleep(0.3) # 비동기적 지연/I/O 발생 시뮬레이션
			value = self.current
			self.current += 1
			return value
		else:
			raise StopAsyncIteration # 비동기 반복 종료 신호

async def main():
	print("--- 비동기 이터레이터 순회 시작 ---")
	# 비동기 반복자(async for)를 사용하여 비동기 이터레이터 순회
	async for num in AsyncNumberIterator(4):
		print(f"가져온 숫자: {num}")
	print("--- 비동기 이터레이터 순회 종료 ---")

if __name__ == "__main__":
	asyncio.run(main())