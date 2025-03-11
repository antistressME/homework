from src.filters import filter_by_str, filter_dy_description


def test_filter_by_str(transactions, transactions_filtred):
    result = filter_by_str(transactions, "Перевод организации")
    assert transactions_filtred == result


def test_filter_dy_description(transactions):
    result = filter_dy_description(transactions, ["Перевод организации", "Открытие вклада"])
    count_description = {"Перевод организации": 2, "Открытие вклада": 0}
    assert count_description == result
