import pytest
import fuel

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("4/4") == 100
    assert fuel.convert("0/4") == 0

def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(50) == "50%"

def test_gauge_edges():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(2) == "2%"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(99) == "F"

def test_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")

def test_convert_valueerror():
    # non-numeric
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")

    # numerator > denominator
    with pytest.raises(ValueError):
        fuel.convert("5/4")

    # negative values
    with pytest.raises(ValueError):
        fuel.convert("-1/4")


