def filter_by_currency(transactions: list[dict], currency: str) -> list[dict]:
    """Выдаёт итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    filtered_transaction = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    return filtered_transaction


def transaction_descriptions(transactions: list[dict]) -> list[dict]:
    """Возвращает описание каждой операции по очереди"""
    description = [x["description"] for x in transactions]
    return description
