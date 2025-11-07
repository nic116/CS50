
from bank import value


def test_value_zero():
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_value_twenty():
    assert value("hi") == 20
    assert value("HI") == 20

def test_value_hundred():
    assert value("diuashfphae") == 100
    assert value("MORNING") == 100
