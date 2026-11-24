import pytest
from day1.problem2 import add_return

def test_return():
    assert add_return(3, 2) == 5

def wrong_test():
    assert add_return()

def test_edge_case():
    assert add_return(0, 0) == 0
def wrong_test():
    assert add_return(-5, 5) == 0