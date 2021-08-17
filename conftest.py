import pytest

@pytest.fixture(scope="function")
def print_one():
    print("\n")
    print("A")