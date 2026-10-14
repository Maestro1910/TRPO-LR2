import pytest

from calc import add, div, mod, mul, power, sub


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(7, 4) == 3


def test_mul():
    assert mul(6, 7) == 42


def test_div():
    assert div(10, 4) == 2.5


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)


def test_power():
    assert power(2, 10) == 1024


def test_power_zero():
    assert power(5, 0) == 1


def test_mod():
    assert mod(17, 5) == 2
