import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, transactions_by_usd, transactions_by_rub):
    assert next(filter_by_currency(transactions, "USD")) == transactions_by_usd
    assert next(filter_by_currency([], "USD")) == []
    assert next(filter_by_currency(transactions_by_usd, "RUB")) == []
    assert next(filter_by_currency(transactions, "RUB")) == transactions_by_rub


def test_transaction_descriptions(transactions, descriptions):
    assert next(transaction_descriptions(transactions)) == descriptions
    assert next(transaction_descriptions([])) == []


def test_card_number_generator(card_number):
    assert list(card_number_generator(1, 5)) == card_number
    assert list(card_number_generator(1, 2)) == card_number[:1]
    assert list(card_number_generator(1, 1)) == []
