from unittest.mock import patch

import pandas as pd

from src.read_csv_excel import get_data_by_csv, get_data_by_excel


@patch("src.read_csv_excel.pd.read_csv")
def test_get_data_by_scv(mock_data_csv):
    mock_data_csv.return_value = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    assert get_data_by_csv("123") == [{"No": 131, "Yes": 50}, {"No": 2, "Yes": 21}]
    mock_data_csv.assert_called()
    mock_data_csv.assert_called_once()


def test_get_data_by_csv_shape():
    path_to_file = "../data/transactions.csv"
    assert type(get_data_by_csv(path_to_file)) == list


@patch("src.read_csv_excel.pd.read_excel")
def test_get_data_by_excel(mock_data_excel):
    mock_data_excel.return_value = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    assert get_data_by_excel("123") == [{"No": 131, "Yes": 50}, {"No": 2, "Yes": 21}]
    mock_data_excel.assert_called()
    mock_data_excel.assert_called_once()


def test_get_data_by_excel_shape():
    path_to_file = "../data/transactions_excel.xlsx"
    assert type(get_data_by_excel(path_to_file)) == list
