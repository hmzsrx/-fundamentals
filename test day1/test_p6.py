
import pytest
from day1.problem6 import sum_num, average


def test_normal_case():
    assert sum_num([1, 2, 3, 4]) == 10
    assert average([2, 4, 6]) == 4


def test_edge_case():
    assert sum_num([]) == 0
    assert sum_num([-1, -2, -3]) == -6
    assert average([5]) == 5
    assert average([1, 2]) == 1.5

    
def test_wrong_input():
    with pytest.raises(TypeError):
        sum_num("hello")

    with pytest.raises(ValueError):
        average([])

    with pytest.raises(TypeError):
        average("hello")
