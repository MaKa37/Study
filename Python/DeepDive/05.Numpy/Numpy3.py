import numpy as np
import time

# 데이터 크기: 천만 개
size = 10_000_000

# 1. 속도 비교: Python List vs NumPy Array
py_data = list(range(size))
np_data = np.arange(size)

# Python for문 연산 소요 시간
start_time = time.time()
py_result = [x * 2 for x in py_data]
py_time = time.time() - start_time

# NumPy 벡터화 연산 소요 시간
start_time = time.time()
np_result = np_data * 2
np_time = time.time() - start_time

print(f"Python List for문 소요 시간: {py_time:.4f} 초")
print(f"NumPy Array 벡터화 소요 시간: {np_time:.4f} 초")
print(f"NumPy가 대략 {py_time/np_time:.1f}배 더 빠릅니다.\n")

# 2. 메모리 View vs Copy 속도 비교
# View (메모리 주소만 공유)
start_time = time.time()
np_view = np_data[:] 
view_time = time.time() - start_time

# Copy (새로운 메모리 공간 할당)
start_time = time.time()
np_copy = np_data.copy()
copy_time = time.time() - start_time

print(f"NumPy View 생성 시간: {view_time:.6f} 초")
print(f"NumPy Copy 생성 시간: {copy_time:.6f} 초")