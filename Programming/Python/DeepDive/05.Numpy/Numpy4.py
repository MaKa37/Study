import numpy as np

# 1. 임의의 입력 데이터와 모델 파라미터 초기화
inputs = np.array([1.2, 0.5, -0.8])    # 입력 데이터 (특성 3개)
weights = np.random.randn(3, 4)        # 가중치 행렬 (3개의 입력을 받아 4개의 노드로 전달)
bias = np.array([0.1, -0.2, 0.5, 0.0]) # 편향 (Bias)

# 2. 행렬 내적 연산 및 편향 덧셈 (벡터화 연산으로 for문 없이 즉시 연산)
output = (inputs @ weights) + bias

# 3. 활성화 함수(ReLU) 적용: 0 이하의 값은 0으로 변환 (Clipping)
activation_output = np.maximum(0, output)

print("신경망 계층 통과 후 출력값:", activation_output)
print("*" * 40)

# 임의의 FHD(1080x1920) 해상도 컬러 이미지 픽셀 생성 (RGB 3채널, 0~255)
# (실무에서는 cv2.imread() 등을 통해 실제 이미지를 NumPy 배열로 불러옵니다)
image_rgb = np.random.randint(0, 256, size=(1080, 1920, 3), dtype=np.uint8)

# 1. 특정 색상 채널 슬라이싱 (Red 채널 데이터만 추출)
red_channel = image_rgb[:, :, 0]

# 2. 고속 명암비 조정 (모든 픽셀 값을 1.2배 밝게 조정, 255 초과 방지)
brighter_image = np.clip(image_rgb * 1.2, 0, 255).astype(np.uint8)

# 3. RGB를 그레이스케일로 변환 (R, G, B 채널 방향인 axis=2 기준 평균값 계산)
grayscale_image = np.mean(image_rgb, axis=2).astype(np.uint8)

print(f"원본 RGB 이미지 형태: {image_rgb.shape}")
print(f"그레이스케일 이미지 형태: {grayscale_image.shape}")