import pandas as pd

# 1. 서로 다른 두 개의 데이터 프레임 생성
users = pd.DataFrame({
    'user_id': [101, 102, 103],
    'name': ['Kim', 'Lee', 'Park'],
    'signup_year': [2020, 2021, 2022]
})

purchases = pd.DataFrame({
    'purchase_id': [1, 2, 3, 4, 5],
    'user_id': [101, 101, 103, 102, 101],
    'amount': [50000, 30000, 120000, 45000, 20000]
})

# 2. 공통 키인 'user_id'를 기준으로 두 테이블 병합 (Inner Join)
merge_df = pd.merge(purchases, users, on='user_id')

# 3. 사용자 이름(name)을 기준으로 그룹화하여 구매액(amount) 총합 계산
total_spent = merge_df.groupby('name')['amount'].sum().reset_index()

print("--- 사용자 별 구매 총액 ---")
print(total_spent)

# 4. 총 구매액을 기준으로 내림차순 정렬하여 VIP 순위 도출
vip_customers = total_spent.sort_values(by='amount', ascending=False)

print("--- VIP 고객 누적 구매액 순위 ---")
print(vip_customers)