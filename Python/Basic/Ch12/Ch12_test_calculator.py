# test_calculator.py
import pytest
from Python.Basic.Ch12.Ch12_calculator import add, divide

def test_add():
    """
    정상적인 입력값에 대해 정확한 연산 결과를 반환하는지 검증합니다.
    이 테스트 자체로 'add 함수는 2와 3을 넣으면 5를 반환해야 한다'는 
    정확한 [기능 명세서] 역할을 수행합니다.
    """
    # 파이썬 내장 assert 문을 활용하여 기대값과 실제 실행값을 비교
    assert add(2, 3) == 5

def test_divide_by_zero():
    """
    외부 요인(잘못된 사용자 입력 등)으로 인해 0이 입력되었을 때,
    준비해둔 안전장치(예외 처리)가 정상적으로 작동하는지 테스트합니다.
    """
    # pytest.raises를 사용하여 ValueError가 정상적으로 격발되는지 추적
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # 에러 발생 시 출력되는 상세 메시지(Traceback)가 의도와 일치하는지 2차 검증
    assert str(excinfo.value) == "0으로 나눌 수 없습니다."