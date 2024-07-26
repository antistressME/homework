import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, transactions_by_usd, transactions_by_rub):
    assert filter_by_currency(transactions, "USD") == transactions_by_usd
    assert filter_by_currency([], "USD") == []
    assert filter_by_currency(transactions_by_usd, "RUB") == []
    assert filter_by_currency(transactions, "RUB") == transactions_by_rub


def test_transaction_descriptions(transactions, descriptions):
    assert transaction_descriptions(transactions) == descriptions
    assert transaction_descriptions([]) == []
