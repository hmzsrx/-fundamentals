import pytest
from day3.problem2 import index_of

def test_index_of():
    assert index_of([10, 20, 30, 40], 30) == 2
    assert index_of([5, 8, 12], 5) == 0
    assert index_of([1, 2, 3], 9) == -1


test_index_of()