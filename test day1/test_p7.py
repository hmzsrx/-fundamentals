
import pytest
from day1.problem7 import count_vowels


def test_normal_case():
    assert count_vowels("hello") == 2
    assert count_vowels("Hamza") == 2
    assert count_vowels("education") == 5

def test_edge_case():
    assert count_vowels("") == 0
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("aA") == 2


def test_wrong_input():
    with pytest.raises(TypeError):
        count_vowels(123)

    with pytest.raises(TypeError):
        count_vowels(None)
