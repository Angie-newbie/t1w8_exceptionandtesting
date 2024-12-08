def test_success():
    assert 10 / 2 == 5

def test_fail():
    assert 10 / 2 == 2

def test_exception():
    if True:
        raise ValueError('you got a value error')