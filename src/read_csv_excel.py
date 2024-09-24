import os

import pandas as pd


def get_data_by_csv(path_to_file: str) -> None:
    """Получение информации об операциях из csv файла"""
    path = os.path.abspath(path_to_file)
    csv_data = pd.read_csv(path, delimiter=";")
    return csv_data


if __name__ == "__main__":
    path_to_file = "../data/transactions.csv"
    df1 = get_data_by_csv(path_to_file)
    print(df1.shape)


def get_data_by_excel(path_to_file: str) -> None:
    """Получение информации об операциях из excel файла"""
    path = os.path.abspath(path_to_file)
    xlsx_data = pd.read_excel(path)
    return xlsx_data


if __name__ == "__main__":
    path_to_file = "../data/transactions_excel.xlsx"
    df2 = get_data_by_excel(path_to_file)
    print(df2.shape)
