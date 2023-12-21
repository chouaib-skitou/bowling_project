# tests/test_sum.py

from main import sum

def test_sum():
    assert sum(2, 2) == 4
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0
