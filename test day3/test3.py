import pytest
from day3.problem3 import digit_sum

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(4567) == 22
    assert digit_sum(0) == 0

def test_digit_sum_negative():
    try:
        digit_sum(-123)
        assert False, "Expected ValueError"
    except ValueError:
        assert True