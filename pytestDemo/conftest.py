import pytest


@pytest.fixture
def database():
    # SETUP
    print("Connecting to database")

    yield

    # TEARDOWN
    print("Closing database connection")


# ______________________________________________________________

# To run once before the all test case and teardown after all the test case done.

@pytest.fixture(scope="class")
def database_class():
    # SETUP
    print("Connecting to database")

    yield

    # TEARDOWN
    print("Closing database connection")


@pytest.fixture
def login_data():
    return [
        ("admin", "admin123"),
        ("user1", "user123"),
        ("tester", "test123")
    ]