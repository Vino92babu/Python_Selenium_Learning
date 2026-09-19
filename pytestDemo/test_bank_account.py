import pytest


@pytest.mark.smoke
def test_deposit():
    balance = 10000
    deposit = 5000

    balance = balance + deposit

    assert balance == 15000


@pytest.mark.regression
def test_withdrawal():
    balance = 10000
    withdrawal = 3000

    balance = balance - withdrawal

    assert balance == 7000


@pytest.mark.smoke
def test_balance():
    balance = 25000

    assert balance == 25000


@pytest.mark.regression
def test_minimum_balance():
    balance = 5000

    assert balance >= 1000


@pytest.mark.skip(reason="Functionality is not ready")
def test_transfer():
    balance = 10000
    transfer = 2000

    balance = balance - transfer

    assert balance == 8000