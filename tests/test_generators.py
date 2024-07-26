import pytest

from src.generators import filter_by_currency


def test_filter_by_currency(transactions, transactions_by_usd, transactions_by_rub):
    assert filter_by_currency(transactions, "USD") == transactions_by_usd
    assert filter_by_currency([], "USD") == []
    assert filter_by_currency(transactions_by_usd, "RUB") == []
    assert filter_by_currency(transactions, "RUB") == transactions_by_rub