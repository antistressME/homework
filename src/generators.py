def filter_by_currency(transactions, currency):
    """Выдаёт итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    filtered_transaction = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    return filtered_transaction



