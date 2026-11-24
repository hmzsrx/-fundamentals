
import pytest
from day1.problem5 import max_of_three


def test_normal_case():
    assert max_of_three(10, 20, 30) == 30
    assert max_of_three(50, 20, 10) == 50
    assert max_of_three(10, 40, 20) == 40

def test_edge_case():
    assert max_of_three(5, 5, 5) == 5
    assert max_of_three(-10, -5, -20) == -5
    assert max_of_three(0, 0, 10) == 10

def test_wrong_input():
    with pytest.raises(TypeError):
        max_of_three("hello", 10, 20)
