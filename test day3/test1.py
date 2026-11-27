import pytest
from day3.problem1 import count_down

def test_count_down():
    assert count_down(5) == [5, 4, 3, 2, 1]
    assert count_down(3) == [3, 2, 1]
    assert count_down(1) == [1]

test_count_down()
