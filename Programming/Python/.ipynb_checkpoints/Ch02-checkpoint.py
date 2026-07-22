# 1. 조건문(Conditional Statements)

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

# 3. 흐름 이동 및 함수 제어

# 3.1 break, continue, pass

# 3.2.1. break: 조건을 만족하면 루프를 즉시 '탈출'
count_break = 0
while count_break < 5:
    count_break += 1
    if count_break == 3:
        break
    print(f"break문 출력 번호: {count_break}")

print("-" * 30)

# 3.2.2. continue: 조건을 만족하면 이번 차례만 '건너뛰고' 다음 반복 진행
count_continue = 0
while count_continue < 5:
    count_continue += 1
    if count_continue == 3:
        continue
    print(f"continue문 출력 번호: {count_continue}")

print("-" * 30)

# 3.2.3. pass: 조건을 만족해도 아무 일 없다는 듯 '그냥 통과'
count_pass = 0
while count_pass < 5:
    count_pass += 1
    if count_pass == 3:
        pass
    print(f"pass문 출력 번호: {count_pass}")

# 3.3 함수 수준의 제어
num_list1 = [1, "3", "A"]
num_list2 = [2, "4", "B"]

# 3.3.1 return
def check_list(list):
    # 조건문 true 시 return 되어 함수 실행 종료됨.
    for item in list:
        if item % 2 == 1: # 2로 나눈 나머지가 1일 시 홀수
            return "홀수"
        if item % 2 == 0: # 2로 나눈 나머지가 0일 시 짝수
            return "짝수"

print(check_list(num_list1)) # 출력 값: 홀수
print(check_list(num_list2)) # 출력 값: 짝수

# 3.3.2 yield
def generator_exam():
    # 1. 첫 번째 구간
    print("[함수 내부] ─── 1번 구간 시작")
    local_count = 1  # 함수 내 지역 변수 상태 유지 확인용
    print(f"[함수 내부] 현재 local_count 값: {local_count}")
    yield "첫 번째 반환값 (A)"  # 여기서 일시 중지! 제어권을 호출자에게 넘김
    
    # 2. 두 번째 구간
    print("[함수 내부] ─── 2번 구간 시작 (멈췄던 곳에서 재개됨)")
    local_count += 1  # 이전의 local_count(1) 상태가 그대로 유지되어 있음
    print(f"[함수 내부] 현재 local_count 값: {local_count}")
    yield "두 번째 반환값 (B)"  # 여기서 다시 일시 중지!
    
    # 3. 세 번째 구간
    print("[함수 내부] ─── 3번 구간 시작")
    print("[함수 내부] 이제 더 이상 yield할 값이 없습니다.")
    # yield가 없으므로 함수가 완전히 종료됨 (StopIteration 발생)

# ==========================================
# 실행 및 동작 흐름 확인
# ==========================================

# 1. 제너레이터 객체 생성
# 주의: 함수를 호출해도 내부 코드(print문 등)는 전혀 실행되지 않고 객체만 만들어집니다.
gen = generator_exam()
print(f"생성된 객체 타입: {type(gen)}")
print("-" * 40)

# 2. 첫 번째 next() 호출
print("★ [호출자] 첫 번째 next() 호출")
result1 = next(gen)
print(f"★ [호출자] 받아온 값: {result1}")
print("-" * 40)

# 3. 두 번째 next() 호출
print("★ [호출자] 두 번째 next() 호출")
result2 = next(gen)
print(f"★ [호출자] 받아온 값: {result2}")
print("-" * 40)

# 4. 세 번째 next() 호출 (더 이상 yield가 없을 때)
print("★ [호출자] 세 번째 next() 호출")
try:
    result3 = next(gen)
except StopIteration:
    print("★ [호출자] 예외 발생: 함수가 끝까지 실행되어 StopIteration이 던져졌습니다.")

# 4. 고급 흐름 제어

## 4.1 예외 처리
def divide_numbers(num1, num2):
    print(f"--- 입력값: {num1}, {num2} ---")

    try:
        # 예외 발생 가능성이 있는 코드
        result = num1 / num2        

    except ZeroDivisionError:
        # 0으로 나누었을 때 발생하는 구체적인 예외 처리
        print("except 블록: 0으로 나눌 수 없습니다. (ZeroDivisionError)")

    except TypeError:
        # 숫자가 아닌 값을 입력했을 때 발생하는 구체적인 예외 처리
        print("except 블록: 숫자 타입만 연산이 가능합니다. (TypeError)")

    except Exception as e:
        # 그 외 예상치 못한 예외 처리(모범 사례에 따라 구체적 예외 처리 후 마지막에 배치)
        print(f"except 블록: 알 수 없는 오류가 발생했습니다. ({e})")
    
    else:
        # 예외가 발생하지 않았을 때만 실행
        print(f"else 블록: 연산 성공! 결과값은 {result} 입니다.")
    
    finally:
        # 예외 발생 여부와 상관없이 무조건 마지막에 실행
        print("finally 블록: 연산 과정이 종료되었습니다.\n")

# 1. 예외가 발생하지 않는 정상적인 경우
# 흐름: try -> else -> finally
divide_numbers(10, 2)

# 2. 0으로 나누는 예외가 발생하는 경우
# 흐름: try -> except(ZeroDivisionError) -> finally
divide_numbers(10, 0)

# 3. 잘못된 데이터 타입으로 인한 예외가 발생하는 경우
# 흐름: try -> except(TypeError) -> finally
divide_numbers(10, "문자열")
        
# 4. 알 수 없는 오류 발생 시(ex: ValueError / 배열의 크기 차이)
# 흐름: try -> except Exception(ValueError) -> finally
import numpy as np
arr1 = np.array([1, 2])
arr2 = np.array([1, 2, 3])
divide_numbers(arr1, arr2)

# 4.2 예와 발생과 검증

# 1. 커스텀 예외 클래스 정의 (Exception 클래스를 상속)
class NegativePriceError(Exception):
    ### 상품 가격이 음수일 때 발생하는 커스텀 예외 ###
    def __init__(self, price):
        # 부모 클래스(Exception)의 생성자를 호출하여 에러 메시지를 설정합니다.
        super().__init__(f"에러: 가격은 음수가 될 수 없습니다. (입력값: {price}원)")


# 2. raise 활용: 비즈니스 로직에 따른 의도적 예외 발생
def set_product_price(price):
    if price < 0:
        # 입력값이 비즈니스 규칙(가격은 0 이상)에 어긋나면 커스텀 예외를 던집니다.
        raise NegativePriceError(price)
    
    print(f"상품 가격이 {price}원으로 설정되었습니다.")
    return price


# 3. assert 활용: 개발 단계에서의 논리적 상태 검증
def apply_discount(price, discount_rate):
    # 개발자가 'discount_rate는 무조건 0.0 ~ 1.0 사이여야 한다'고 단언(assert)합니다.
    # 만약 이 조건이 False라면 AssertionError를 발생시킵니다.
    assert 0.0 <= discount_rate <= 1.0, f"디버깅 경고: 할인율({discount_rate})이 올바른 범위(0.0~1.0)에 있지 않습니다."
    
    discounted_price = price * (1 - discount_rate)
    print(f"할인 적용 완료: {int(discounted_price)}원")
    return int(discounted_price)


# ==========================================
# 실행 및 결과 확인
# ==========================================

print("--- [테스트 1] 정상적인 경우 ---")
price1 = set_product_price(10000)
apply_discount(price1, 0.2)  # 20% 할인 정상 적용

print("\n--- [테스트 2] raise 작동 확인 (비정상적인 가격) ---")
try:
    set_product_price(-5000)
except NegativePriceError as e:
    # raise로 던진 커스텀 예외를 여기서 잡아 처리합니다.
    print(e)

print("\n--- [테스트 3] assert 작동 확인 (비정상적인 할인율) ---")
try:
    # 할인율을 2.0 (200%)으로 잘못 입력한 경우
    apply_discount(10000, 2.0)
except AssertionError as e:
    # assert 조건이 False가 되어 AssertionError가 발생합니다.
    print(e)

# 4.3 컨텍스트 관리
# 1. 커스텀 예외 클래스 정의 (Exception 클래스를 상속)
class NegativePriceError(Exception):
    """상품 가격이 음수일 때 발생하는 커스텀 예외"""
    def __init__(self, price):
        # 부모 클래스(Exception)의 생성자를 호출하여 에러 메시지를 설정합니다.
        super().__init__(f"에러: 가격은 음수가 될 수 없습니다. (입력값: {price}원)")


# 2. raise 활용: 비즈니스 로직에 따른 의도적 예외 발생
def set_product_price(price):
    if price < 0:
        # 입력값이 비즈니스 규칙(가격은 0 이상)에 어긋나면 커스텀 예외를 던집니다.
        raise NegativePriceError(price)
    
    print(f"상품 가격이 {price}원으로 설정되었습니다.")
    return price


# 3. assert 활용: 개발 단계에서의 논리적 상태 검증
def apply_discount(price, discount_rate):
    # 개발자가 'discount_rate는 무조건 0.0 ~ 1.0 사이여야 한다'고 단언(assert)합니다.
    # 만약 이 조건이 False라면 AssertionError를 발생시킵니다.
    assert 0.0 <= discount_rate <= 1.0, f"디버깅 경고: 할인율({discount_rate})이 올바른 범위(0.0~1.0)에 있지 않습니다."
    
    discounted_price = price * (1 - discount_rate)
    print(f"할인 적용 완료: {int(discounted_price)}원")
    return int(discounted_price)


# ==========================================
# 실행 및 결과 확인
# ==========================================

print("--- [테스트 1] 정상적인 경우 ---")
price1 = set_product_price(10000)
apply_discount(price1, 0.2)  # 20% 할인 정상 적용

print("\n--- [테스트 2] raise 작동 확인 (비정상적인 가격) ---")
try:
    set_product_price(-5000)
except NegativePriceError as e:
    # raise로 던진 커스텀 예외를 여기서 잡아 처리합니다.
    print(e)

print("\n--- [테스트 3] assert 작동 확인 (비정상적인 할인율) ---")
try:
    # 할인율을 2.0 (200%)으로 잘못 입력한 경우
    apply_discount(10000, 2.0)
except AssertionError as e:
    # assert 조건이 False가 되어 AssertionError가 발생합니다.
    print(e)