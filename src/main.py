import re

from filters import filter_by_str
from generators import filter_by_currency, transaction_descriptions
from processing import filter_by_state, sort_by_date
from read_csv_excel import get_data_by_csv, get_data_by_excel
from utils import get_list
from widget import get_date, mask_account_card


def main_func():
    """Отвечает за основную логику проекта"""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
        user_chois = int(input())
        if user_chois == 1:
            print("Для обработки выбран JSON-файл.")
            transactions = get_list("operations.json")
            break
        elif user_chois == 2:
            print("Для обработки выбран CSV-файл.")
            transactions = get_data_by_csv("../data/transactions.csv")
            break
        elif user_chois == 3:
            print("Для обработки выбран XLSX-файл.")
            transactions = get_data_by_excel("../data/transactions_excel.xlsx")
            break
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_status = str(input())
        if user_status.upper() in "EXECUTED, CANCELED, PENDING":
            break
        print(f'Статус операции "{user_status}" недоступен.')
    transactions_by_state = filter_by_state(transactions, user_status.upper())
    print("Отсортировать операции по дате? Да/Нет")
    sorted_by_date = str(input()).lower()
    if sorted_by_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sorted_by_increase = str(input()).lower()
        if sorted_by_increase.lower() in "по возрастанию":
            sorted_transactions = sort_by_date(transactions_by_state, reverse=False)
        else:
            sorted_transactions = sort_by_date(transactions_by_state)
    else:
        sorted_transactions = transactions_by_state
    print("Выводить только рублевые тразакции? Да/Нет")
    rubles_transactions = str(input()).lower()
    if rubles_transactions == "да":
        transactions = []
        for item in sorted_transactions:
            if re.search("RUB", str(item)):
                transactions.append(item)
    else:
        transactions = sorted_transactions
    print(
        """Отфильтровать список транзакций по определенному слову 
    в описании? Да/Нет"""
    )
    filter_by_word = str(input())
    if filter_by_word.lower() == "да":
        print("Введите слово")
        word = str(input())
        transactions = filter_by_str(transactions, word)
    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            operation_data = get_date(transaction["date"])
            transaction_to = mask_account_card(transaction["to"])
            description = transaction["description"]
            if user_chois == 1:
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]
            else:
                amount = transaction["amount"]
                currency = transaction["currency_code"]
            if transaction.get("from"):
                transaction_from = mask_account_card(str(transaction["from"]))
            else:
                transaction_from = ""
            print(
                f"{operation_data} {str(description)}\n{transaction_from} -> {transaction_to}\nСумма: {amount} {currency}"
            )


if __name__ == "__main__":
    main_func()
