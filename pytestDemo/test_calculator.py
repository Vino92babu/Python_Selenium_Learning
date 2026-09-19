import pytest


@pytest.mark.smoke
def test_addition():
    a = 10
    b = 5
    result = a + b

    assert result == 15


@pytest.mark.smoke
def test_subtraction():
    a = 10
    b = 5
    result = a - b

    assert result == 5


@pytest.mark.regression
def test_multiplication():
    a = 10
    b = 5
    result = a * b

    assert result == 50


@pytest.mark.regression
def test_division():
    a = 10
    b = 5
    result = a / b

    assert result == 2