import pytest
from day2.problem7 import invert

def test_invert():

    # Normal case
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    # Edge case
    assert invert({}) == {}

    # Wrong case
    with pytest.raises(ValueError):
        invert({"a": 1, "b": 1})