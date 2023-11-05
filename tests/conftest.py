import pytest

from pyplayht.classes import Client


@pytest.fixture
def client() -> Client:
    return Client()
