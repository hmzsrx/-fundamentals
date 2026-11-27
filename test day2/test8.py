import pytest
from day2.problem8 import most_common_word


def test_most_common_word():
    assert most_common_word("The cat sat. The dog ran!") == "the"


def test_ignore_case_and_punctuation():
    assert most_common_word("Cat? cat, CAT. dog") == "cat"


def test_alphabetical_tie():
    assert most_common_word("b a b a") == "a"