import pytest
from day2.problem3 import remove_duplicates

def test_remove_duplicates():

    # Normal case
    assert remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]

    # Edge case (empty list)
    assert remove_duplicates([]) == []

    # Wrong input
    assert remove_duplicates(None) == []