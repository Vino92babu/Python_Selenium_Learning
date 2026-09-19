import pytest


# @pytest.fixture
# def database():
#     # SETUP
#     print("Connecting to database")

#     yield

#     # TEARDOWN
#     print("Closing database connection")


# def test_get_customer(database):
#     print("Get customer details")
#     assert True


# def test_create_customer(database):
#     print("Create customer")
#     assert True

# __________________________________________________________



@pytest.mark.usefixtures("database_class")
class Test_DB:
    def test_get_customer(self):
        print("Get customer details")
    assert True


    def test_create_customer(self):
        print("Create customer")
    assert True

