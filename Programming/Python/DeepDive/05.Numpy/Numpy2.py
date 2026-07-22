import numpy as np

print('-' * 50)

# 0부터 9까지의 수열 생성
print(f"seq_arrㅣ{np.arange(10)}")

# 0으로 채워진 3x3 행렬 생성
print(f"zero_matrixㅣ{np.zeros((3, 3))}")

# 표준 정규 분포를 따르는 난수 생성 (머신러닝 가중치 초기화에 자주 사용)
print(f"random_weightsㅣ{np.random.randn(2, 2)}")

print('-' * 50)

# 1차원 배열을 2행 5열의 2차원 행렬로 형태 변환
arr_1d = np.arange(10)
arr_2d = arr_1d.reshape((2, 5))
print(arr_1d, "\n", arr_2d)

# 데이터 타입 형변환 (메모리 사용량 감소)
arr_float= arr_2d.astype(np.float32)
print(arr_float)

print('-' * 50)

data = np.array([10, -5, 20, -1, 30])

# 불리언 인덱싱: 0보다 큰 데이터만 추출
positive_data = data[data > 0]  # 결과: [10, 20, 30]
print(positive_data)

# 팬시 인덱싱: 0, 2, 4번째 인덱스 데이터 한 번에 추출
selected_data = data[[0, 2, 4]]  # 결과: [10, 20, 30]
print(selected_data)

print('-' * 50)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 수직(행 방향)으로 이어 붙이기 (Vertical Stack)
v_stacked = np.vstack((A, B))

# 수평(열 방향)으로 이어 붙이기 (Horizontal Stack)
h_stacked = np.hstack((A, B))

# 원본 보존을 위한 깊은 복사
safe_copy = A.copy()
print(v_stacked, "\n")
print(h_stacked, "\n")
print(safe_copy)

print('-' * 50)

matrix = np.array([[1, 2, 3], [4, 5, 6]])

# 전체 원소의 합
total_sum = np.sum(matrix)

# 열(Column) 기준의 합 (Axis 0)
col_sum = np.sum(matrix, axis=0) # 결과: [5, 7, 9]

# 행(Row) 기준의 평균 (Axis 1)
row_mean = np.mean(matrix, axis=1) # 결과: [2., 5.]

# 행렬 내적 (Dot Product)
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
dot_product = X @ Y # 또는 np.dot(X, Y)
print(dot_product)

print('-' * 50)

