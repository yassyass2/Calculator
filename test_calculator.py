import pytest
from Calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)


def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)


def test_product(calculator):
    assert 32 == calculator.product(8, 4)


def test_quotient(calculator):
    assert 5 == calculator.quotient(25, 5)
