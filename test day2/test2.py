import pytest 
from day2.problem2 import second_largest


def test_second_largest():

    #  Normal case
    assert second_largest([10, 20, 30, 40]) == 30

    # Edge case (duplicate values)
    assert second_largest([10, 10, 20, 20, 30]) == 20

    # Wrong input (list with one element)
    assert second_largest([10]) == None