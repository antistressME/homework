import pandas as pd
from unittest.mock import patch


def read_csv(path_to_file):
    """Получение списка словарей из csv файла"""
    csv_data = pd.read_csv(path_to_file, delimiter=';')
    return csv_data



if __name__ == '__main__':
    path_to_file = '../data/transactions.csv'
    df = read_csv(path_to_file)
    print(df.shape)


def read_excel(path_to_file):
    """Получение списка словарей из excel файла"""
    xlsx_data = pd.read_excel(path_to_file)
    return xlsx_data


if __name__ == '__main__':
    path_to_file = '../data/transactions_excel.xlsx'
    df = read_excel(path_to_file)
    print(df.head(3), df.shape)


