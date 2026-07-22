import pandas as pd

# Series 생성 예시 (1차원)
ages = pd.Series([25, 32, 28, 41], name="Age")
print(ages)

print('*' * 40)

# DataFrame 생성 예시 (2차원)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 32, 28, 41],
    "City": ["Seoul", "Busan", "Seoul", "Jeju"]
}
df = pd.DataFrame(data)
print(df)

print('*' * 40)

# 'Age'가 30 이상인 데이터만 필터링하여 'Name'과 'City' 컬럼만 추출
filtered_df = df.loc[df['Age'] >= 30, ['Name', 'City']]
print(filtered_df)

print('*' * 40)

# 'Age' 컬럼의 빈칸을 해당 컬럼의 평균값으로 채우기
data2 = {
    "Alpha": ["A", "B"],
    "B": [30, None]
}

df2 = pd.DataFrame(data2)

mean_Age = df['Age'].mean()
df2['B'] = df2['B'].fillna(mean_Age)
print(df2)

print('*' * 40)

# 'City'별로 그룹화하여 'Age'의 평균(mean) 구하기
dept_age = df.groupby('City')['Age'].mean()
print(dept_age)