import pandas as pd
import json

from src.read_csv_excel import read_csv, read_excel
from unittest.mock import patch



def test_read_csv_shape():
    path_to_file = '../data/transactions.csv'
    csv_data = read_csv(path_to_file)
    assert csv_data.shape == (1000, 9)



