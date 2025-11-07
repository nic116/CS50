import pytest
from fuel import convert, gauge


def test_convert_good_numbers():
    assert convert("1/2") == 50
    assert convert("0/2") == 0
    assert convert("1/1") == 100
    assert convert("1/3") == 33

def test_convert_nonnumeric():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_topheavy():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_E_F():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_middle():
    assert gauge(2) == "2%"
    assert gauge(10) == "10%"
    assert gauge(60) == "60%"