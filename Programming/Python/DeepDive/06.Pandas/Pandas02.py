import pandas as pd

# 1. 지저분한 로그 데이터 생성
raw_data = {
    'user_log': [
        "Alice Smith - alice@email.com - 010-1234-5678  ",
        "Bob Jones - bob@email.com - 010-9876-5432",
        "Charlie Brown - charlie@email.com - 010-5555-5555 "
    ]
}
df = pd.DataFrame(raw_data)

# 2. '-' 기준으로 텍스트 분할 (expand=True 옵션으로 새로운 DataFrame 반환)
split_data = df['user_log'].str.split(' - ', expand=True)

# 3. 분할된 데이터를 새로운 컬럼으로 할당 및 앞뒤 공백(strip) 제거
df['Name'] = split_data[0].str.strip()
df['Email'] = split_data[1].str.strip()
df['Phone'] = split_data[2].str.strip()

# 4. 불필요해진 원본 로그 컬럼 삭제
df = df.drop(columns=['user_log'])

print("--- 정제 완료된 데이터 ---")
print(df)