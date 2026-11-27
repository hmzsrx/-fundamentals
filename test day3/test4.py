import pytest
from day3.problem4 import first_negative

def test_first_negative():
    assert first_negative([2, 4, -5, -8]) == -5
    assert first_negative([-3, 5, -7]) == -3
    assert first_negative([1, 2, 3, 4]) is None

test_first_negative()