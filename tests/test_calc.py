import pytest

from app.calc import add, fizzbuzz


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    ("n", "expected"),
    [(1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
