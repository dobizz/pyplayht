import pytest

from mymodule import myfunction


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, 2, 3, 4, 5], 15),
    ],
)
def test_myfunction(test_input, expected):
    assert myfunction(*test_input, expected)
