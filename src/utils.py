import json
import os

from src.external_api import currency_conversion


def get_list(file_json: str) -> list[dict]:
    """Преобразуем json файл в список словарей"""
    transact_list = []
    path = os.path.dirname(__file__)[:-4]
    way_to_file = os.path.join(path, "data", file_json)
    with open(way_to_file, "r", encoding="UTF8") as file:
        transaction = json.load(file)
        if type(transaction) == list:
            transact_list = transaction
    return transact_list


def get_amount(operation: dict) -> float:
    """Рассчитываем сумму транзакции в рублях"""
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        amount = currency_conversion(amount, currency)
    return float(amount)
