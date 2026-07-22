import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BANK_OF_KOREA_API_KEY")
# 1번부터 100번까지의 통계 목록 요청
url = f"https://ecos.bok.or.kr/api/StatisticTableList/{API_KEY}/json/kr/1/100"
print(url)

response = requests.get(url)
data = response.json()

if "StatisticTableList" in data:
    rows = data["StatisticTableList"]["row"]
    for row in rows:
        print(f"코드: {row['STAT_CODE']} | 통계표명: {row['STAT_NAME']} | 주기: {row['CYCLE']}")
else:
    print("API 호출 실패:", data)