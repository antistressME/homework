from unittest.mock import Mock

from src.utils import get_amount, get_list


def test_get_list(transact_list_0):
    transact_list = get_list("operations.json")
    operation = transact_list[0]
    assert operation == transact_list_0


def test_get_list(transact_list_1):
    transact_list = get_list("operations.json")
    operation = transact_list[1]
    assert operation == transact_list_1


def test_get_amount_rub(transact_list_0):
    operation = get_amount(transact_list_0)
    assert operation == 31957.58


def test_conversion():
    mock_currency = Mock(return_value=150.39)
    currency_conversion = mock_currency
    assert currency_conversion(12, "USD") == 150.39
    mock_currency.assert_called_once()
