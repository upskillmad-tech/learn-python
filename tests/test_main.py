import pytest
from main import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (-1, -1, -2),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, -1),
        (-1, 1, -2),
        (-1, -1, 0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-1, 1, -1),
        (-1, -1, 1),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (18, 3, 6),
        (-1, 1, -1),
        (-1, -1, 1),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected
    with pytest.raises(ValueError):
        divide(1, 0)
