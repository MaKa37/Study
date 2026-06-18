# 1. 조건문(Conditional Statements)

"""
## 1.1 if, elif, else
c_list = [True, 90, 85, 77, 100, 60, 73, False] # True = 1, False = 0으로 비교 가능한데, None은 비교할 수 없어서 TypeError 발생함.
count = 0

for item in c_list:
    count += 1
    if item >= 90:
        print(f"Count:{count} ㅣ 90점 이상")
    elif item >= 80:
        print(f"Count:{count} ㅣ 80점 이상") # 조건 >= 80 < 90 과 동일
    else:
        print(f"Count:{count} ㅣ 그 외 점수")

## 1.2 Truthy와 Falsy & 단축평가
f_list = [0, "", '', None, [], {}] # False로 명시하지 않아도 False인 데이터
for item in f_list:
    print(f"{item}의 boolean 판정 값: {bool(item)}")

# 1.3 조건부 표현식 삼항 연산자
animal = "cat"
cat_bool = True if animal == "cat" else False
print(cat_bool) # True


## 1.4 왈러스 연산자
if(n := len(f_list)) > 5:
    print(True)

## 1.4.2 왈러스 연산자 + 삼항 연산자
print(True if(n := len(f_list)) > 10 else False)

## 1.5 구조적 패턴 매칭
command = ["move", 10, 20]
match command:
    case ["move", x, y]:
        print(f"좌표 {x}, {y}로 이동")
    case _: # default 역할 / _ 기호는 나머지 전부를 의미함.
        print("알 수 없는 명령어")

# 2. 반복문

## 2.1 순회형 반복
for i, name in enumerate(["Alice", "Bob"]):
    print(f"{i}번째 이름: {name}")

## 2.2 조건형 반복(while)
count = 0
while count < 3:
    print(count)
    count += 1
"""
## 2.3 컴프리헨션과 제너레이터
import sys

# 1천만 개의 데이터를 다루는 경우
list_comp = [x for x in range(10000000)]
gen_expr = (x for x in range(10000000))

print(f"리스트 메모리: {sys.getsizeof(list_comp):,} 바이트")
print(f"제너레이터 메모리: {sys.getsizeof(gen_expr):,} 바이트")

# --- 예상 출력 결과 ---
# 리스트 메모리: 89,095,160 바이트 (약 89MB)
# 제너레이터 메모리: 104 바이트 (크기와 무관하게 고정)
