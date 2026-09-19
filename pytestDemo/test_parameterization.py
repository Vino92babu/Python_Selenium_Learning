'''Login test WITHOUT parameterization'''
def test_valid_login():
    username = "admin"
    password = "admin123"

    assert username == "admin"
    assert password == "admin123"


def test_user_login():
    username = "user1"
    password = "user123"

    assert username == "user1"
    assert password == "user123"


def test_invalid_login():
    username = "wrong"
    password = "wrong123"

    assert username != "admin"
    assert password != "admin123"

# ___________________________________________________________________________________________

'''Login test WITH parameterization'''

import pytest

@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("user1", "user123"),
    ("tester", "test123"),
])

def test_login(username, password):
    print(f"Username: {username}")
    print(f"Password: {password}")

    assert username is not None
    assert password is not None