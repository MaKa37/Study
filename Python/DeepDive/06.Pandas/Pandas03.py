import pandas as pd

# 1. 일별 매출 데이터 생성 (날짜가 문자열임)
sales_data = {
    'date': ['2023-10-01', '2023-10-15', '2023-10-31', '2023-11-05', '2023-11-20'],
    'sales_amount': [1000, 2000, 1500, 3000, 2500]
}
df = pd.DataFrame(sales_data)

# 2. 날짜 문자열을 datetime 타입으로 변환 후 인덱스로 설정 (시계열 분석의 핵심)
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# 3. 커스텀 할인 함수 정의 및 적용 (apply 활용)
# 예: 2000 이상인 매출은 10% 할인을 적용하는 로직
def apply_discount(amount):
    if amount >= 2000:
        return amount * 0.9
    return amount

df['final_sales'] = df['sales_amount'].apply(apply_discount)

# 4. 월별(Month)로 리샘플링하여 총매출(sum) 계산
monthly_sales = df.resample('ME').sum() # 'M'은 월말 기준(최신 버전은 'ME' 권장)

print("--- 월별 최종 매출 집계 ---")
print(monthly_sales[['final_sales']])