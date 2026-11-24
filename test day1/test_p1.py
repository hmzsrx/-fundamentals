import pytest
from day1.problem1 import check_number

def test_check_num():
    assert check_number(5) == "positive"
    assert check_number(-5) == "negative"
    assert check_number(0) == "zero"

test_check_num() 