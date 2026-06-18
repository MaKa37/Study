# 1. 숫자형 (Numeric Type)
val_int = 10
val_float = 3.14
val_complex = 1 + 2j

# 2. 시퀀스형 (Sequence Type)
val_str = "hello"
val_list = [1, 2, 3]
val_tuple = (1, 2, 3)
val_range = range(1, 10)

# 3. 매핑형 (Mapping Type)
val_dict = {"name": "Tom", "age": 20}

# 4. 집합형 (Set Type)
val_set = {1, 2, 3}
val_frozenset = frozenset({1, 2, 3})

# 5. 불리언형 (Boolean Type)
val_bool = True

# 6. None 타입 (NoneType)
val_none = None

# 7. 바이너리형 (Binary Type)
val_bytes = b'hello'
val_bytearray = bytearray(5)
val_memoryview = memoryview(b'hello')

# 타입 출력 확인
data_list = [
    val_int, val_float, val_complex, val_str, val_list, val_tuple, 
    val_range, val_dict, val_set, val_frozenset, val_bool, 
    val_none, val_bytes, val_bytearray, val_memoryview
]

for item in data_list:
    print(f"Value: {item} | Type: {type(item)}")


# 연산자 결합성 확인용 샘플 코드
print("\n산술 연산자")
print("1) 좌결합성: 같은 우선순위면 왼쪽에서 오른쪽으로 계산")
print("-" * 50)

# 뺄셈: (10 - 4) - 2
result_sub = 10 - 4 - 2
print("10 - 4 - 2 =", result_sub)  # 4

# 나눗셈과 곱셈: (10 / 2) * 5
result_div_mul = 10 / 2 * 5
print("10 / 2 * 5 =", result_div_mul)  # 25.0

# 덧셈과 뺄셈도 좌결합성
result_add_sub = 20 + 5 - 3
print("20 + 5 - 3 =", result_add_sub)  # 22

print("\n2) 우결합성: 거듭제곱은 오른쪽에서 왼쪽으로 계산")
print("-" * 50)

# 2 ** (3 ** 2)
result_exp = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", result_exp)  # 512

# 비교용: (2 ** 3) ** 2
result_exp_left = (2 ** 3) ** 2
print("(2 ** 3) ** 2 =", result_exp_left)  # 64

print("\n3) 우결합성: 대입 연산")
print("-" * 50)

a = b = c = 10
print("a =", a, ", b =", b, ", c =", c)

print("\n4) 괄호로 결합 순서 직접 비교")
print("-" * 50)

print("10 - (4 - 2) =", 10 - (4 - 2))      # 8
print("10 / (2 * 5) =", 10 / (2 * 5))      # 1.0
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)    # 64

print("\n산술 연산자 결과 확인 완료")
print()

# 논리 연산자 우선순위 / 결합성 확인
print("논리 연산자")
print("1) not > and > or")
print("-" * 40)

a = True
b = False
c = True

# not이 먼저 적용됨
result1 = not a and b
print("not a and b =", result1)  # (not True) and False -> False and False -> False

# and가 or보다 먼저 적용됨
result2 = a or b and c
print("a or b and c =", result2)  # True or (False and True) -> True or False -> True

# 괄호로 비교
result3 = (a or b) and c
print("(a or b) and c =", result3)  # (True or False) and True -> True and True -> True

print("\n2) 결합 순서 확인")
print("-" * 40)

# and, or는 같은 종류끼리 왼쪽에서 오른쪽으로 평가
result4 = True and True and False
print("True and True and False =", result4)  # (True and True) and False -> False

result5 = False or False or True
print("False or False or True =", result5)  # (False or False) or True -> True

print("\n3) 단락 평가(short-circuit) 확인")
print("-" * 40)

def show(name, value):
    print(f"{name} 평가됨")
    return value

print("예시 A: False and ...")
x = show("왼쪽", False) and show("오른쪽", True)
print("결과:", x)

print("\n예시 B: True or ...")
y = show("왼쪽", True) or show("오른쪽", False)
print("결과:", y)

print("\n논리 연산자 결과 확인 완료\n")

a1 = 1
a2 = 3.14
a3 = "Word"
a4 = [1, 2, 3, 4]
a5 = (1, 2, 3, 4)
a6 = {1: 10, 2: 20}
a7 = True
a8 = False
a9 = None


a_List = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
for item in a_List:
    print(f"{item}은 {type(item)}타입 입니다.")