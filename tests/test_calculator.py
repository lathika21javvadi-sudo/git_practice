from calculator import add, sub, mul

def test_add():
    assert add(5, 3) == 8

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(5, 3) == 15
