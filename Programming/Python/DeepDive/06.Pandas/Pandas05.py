import pandas as pd
import numpy as np

# 가상의 30일치 주가 데이터 생성
dates = pd.date_range('2023-01-01', periods=30)
prices = np.random.randint(50000, 60000, size=30)
df_stock = pd.DataFrame({'Close': prices}, index=dates)

# rolling() 메서드를 활용한 5일 이동평균선(5-MA) 도출
df_stock['5-MA'] = df_stock['Close'].rolling(window=5).mean()

print(df_stock.tail())
print('*' * 40)

# 유저들의 행동 로그 데이터
log_data = pd.DataFrame({
    'user_id': ['U1', 'U1', 'U2', 'U3', 'U2'],
    'action': ['view', 'purchase', 'view', 'view', 'cart']
})

# pd.get_dummies()를 이용해 행동을 원핫 인코딩(One-Hot Encoding)으로 변환
action_dummies = pd.get_dummies(log_data['action'])
log_merged = pd.concat([log_data['user_id'], action_dummies], axis=1)

# 유저별로 어떤 행동을 총 몇 번 했는지 요약 (퍼널 분석의 기초)
user_funnel = log_merged.groupby('user_id').sum()
print(user_funnel)