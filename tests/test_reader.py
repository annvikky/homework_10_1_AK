from unittest.mock import patch

from src.reader import read_transactions_from_csv_file, read_transactions_from_excel_file

mock_data = {
    "id": 650703.0,
    "state": "EXECUTED",
    "date": "2023-09-05T11:30:32Z",
    "amount": 16210.0,
    "currency_name": "Sol",
    "currency_code": "PEN",
    "from": "Счет 58803664561298323391",
    "to": "Счет 39745660563456619397",
    "description": "Перевод организации",
}


@patch("pandas.read_csv")
def test_read_transactions_from_csv_file(mock_read_csv):
    """Тест на чтение файла и возврат транзакций."""
    mock_read_csv.return_value.to_dict.return_value = mock_data
    assert read_transactions_from_csv_file("p") == mock_data
    mock_read_csv.assert_called_with("p", sep=None, engine="python")


@patch("pandas.read_csv")
def test_read_transactions_from_csv_empty_file(mock_read_csv):
    """Тест на чтение пустого файла."""
    mock_read_csv.return_value.to_dict.return_value = []
    assert read_transactions_from_csv_file("p") == []
    mock_read_csv.assert_called_with("p", sep=None, engine="python")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_file(mock_read_excel):
    """Тест на чтение файла и возврат транзакций."""
    mock_read_excel.return_value.to_dict.return_value = mock_data
    result = read_transactions_from_excel_file("transactions_excel.xlsx")
    assert result == mock_data


@patch("pandas.read_excel")
def test_read_transactions_from_excel_empty_file(mock_read_excel):
    """Тест на чтение пустого файла."""
    mock_read_excel.return_value.to_dict.return_value = []
    result = read_transactions_from_excel_file("transactions_excel.xlsx")
    assert result == []


def test_read_transactions_from_excel_file_not_found():
    """Тест на чтение файла, отcутствующего по указанному пути."""
    assert read_transactions_from_excel_file("p") == []
