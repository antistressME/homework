from unittest.mock import patch

from src.read_csv_excel import get_data_by_csv, get_data_by_excel


@patch("src.read_csv_excel.pd.read_csv")
def test_get_data_by_scv(mock_data_csv):
    mock_data_csv.return_value = []
    assert get_data_by_csv("123") == []
    mock_data_csv.assert_called()
    mock_data_csv.assert_called_once()


def test_get_data_by_csv_shape():
    path_to_file = "../data/transactions.csv"
    assert get_data_by_csv(path_to_file).shape == (1000, 9)


@patch("src.read_csv_excel.pd.read_excel")
def test_get_data_by_excel(mock_data_excel):
    mock_data_excel.return_value = []
    assert get_data_by_excel("123") == []
    mock_data_excel.assert_called()
    mock_data_excel.assert_called_once()


def test_get_data_by_excel_shape():
    path_to_file = "../data/transactions_excel.xlsx"
    assert get_data_by_excel(path_to_file).shape == (1000, 9)
