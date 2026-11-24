import pytest 
from day1.problem3 import is_even

def test_normal_case():
    assert is_even(4) == True
    assert is_even(7) == False

def test_edge_case():
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-3) == False


def test_wrong_input():
    with pytest.raises(TypeError):
        is_even("hello")