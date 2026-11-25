import pytest
from day2.problem6 import merge_stock

def test_merge_stock():

    # 1. Normal case
    assert merge_stock(
        {"apple": 10, "banana": 5},
        {"apple": 20, "orange": 8}
    ) == {"apple": 30, "banana": 5, "orange": 8}

    # 2. Edge case 
    assert merge_stock({}, {}) == {}

    # 3. Wrong input
    with pytest.raises(TypeError):
        merge_stock(None, {"apple": 10})