import pytest

class Testonething:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, print_one):
        print("setting up")

    def test_one_thing(self):
        print("This is branch1")
        assert True