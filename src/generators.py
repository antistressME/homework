def filter_by_currency(transactions: list[dict], currency: str) -> object:
    """Выдаёт итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    filtered_transaction = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    yield filtered_transaction


def transaction_descriptions(transactions: list[dict]) -> object:
    """Возвращает описание каждой операции по очереди"""
    description = [x["description"] for x in transactions]
    yield description


def card_number_generator(a: int, b: int) -> object:
    """Генерирует номера карт в заданном диапазоне"""
    numbers = list(x for x in range(a, b))
    for number in numbers:
        card_number = ""
        num = str(number)
        step = 0
        for i in range(16):
            if i % 4 == 0 and i != 0:
                card_number += " "
            if len(card_number) > 0:
                if card_number[step] == num:
                    card_number += "0"
            else:
                card_number += num
        step += 1
        yield card_number[::-1]
