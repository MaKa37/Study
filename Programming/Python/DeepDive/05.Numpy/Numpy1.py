import numpy as np

print('-' * 50)
# 1. 파이썬 기본 리스트 방식
py_list = [1, 2, 3, 4, 5]
# py_list * 10  <-- (오류/원치않는 결과) 리스트가 10번 반복되어 길어짐!
result_list = [x * 10 for x in py_list] # List Comprehension 사용 필수
print("Python List 결과:", result_list)
print('-' * 50)

# 2. NumPy ndarray 벡터화 연산 방식
np_array = np.array([1, 2, 3, 4, 5])
result_array = np_array * 10 # for문 없이 배열 전체에 연산이 즉시 적용됨 (벡터화)
print("NumPy Array 결과:", result_array)
print('-' * 50)

# 3. 2차원 배열 (행렬, Matrix) 생성
matrix = np.array([
    [1.5, 2.0, 3.1],
    [4.2, 5.0, 6.8]
])

print(f"배열의 차원수 (ndim): {matrix.ndim}차원") 
# 출력: 2차원

print(f"배열의 형태 (shape): {matrix.shape}")    
# 출력: (2, 3) -> 2행 3열을 의미 (매우 중요⭐️)

print(f"데이터 타입 (dtype): {matrix.dtype}")    
# 출력: float64 (64비트 실수형으로 자동 할당됨)
print('-' * 50)