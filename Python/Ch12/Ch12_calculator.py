# calculator.py
def add(a: int, b: int) -> int:
    """두 숫자를 더하는 기본 기능입니다."""
    return a + b

def divide(a: int, b: int) -> float:
    """
    두 숫자를 나누는 기능입니다.
    
    [실무 관점]
    0으로 나누는 연산은 서버 프로세스를 강제 종료시킬 수 있는 치명적인 에러입니다.
    따라서 시스템이 통제 불능 상태에 빠지기 전에, 
    명시적으로 예외(ValueError)를 발생시켜 안전하게 처리합니다.
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b