
import pytest
from day1.problem4 import grade


def test_normal_case():
    assert grade(95) == "A"
    assert grade(80) == "B"
    assert grade(65) == "C"
    assert grade(50) == "F"

def test_edge_case():
    assert grade(0) == "F"
    assert grade(60) == "C"
    assert grade(75) == "B"
    assert grade(90) == "A"
    assert grade(100) == "A"

def test_wrong_input():
    assert isinstance(grade(-1), ValueError)
    assert isinstance(grade(101), ValueError)
