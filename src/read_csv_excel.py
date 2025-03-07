import os

import pandas as pd


def get_data_by_csv(path_to_file: str) -> None:
    """Получение информации об операциях из csv файла"""
    csv_data = pd.read_csv(path_to_file, delimiter=";")
    csv_dict = csv_data.to_dict("index")
    csv_list = []
    for value in csv_dict.values():
        csv_list.append(dict(value))
    return csv_list


if __name__ == "__main__":
    path_to_file = "../data/transactions.csv"
    df1 = get_data_by_csv(path_to_file)
    print(df1)


def get_data_by_excel(path_to_file: str) -> None:
    """Получение информации об операциях из excel файла"""
    xlsx_data = pd.read_excel(path_to_file)
    xlsx_dict = xlsx_data.to_dict("index")
    xlsx_list = []
    for value in xlsx_dict.values():
        xlsx_list.append(dict(value))
    return xlsx_list


if __name__ == "__main__":
    path_to_file = "../data/transactions_excel.xlsx"
    df2 = get_data_by_excel(path_to_file)
    print(df2)
