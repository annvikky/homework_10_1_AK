from unittest.mock import mock_open, patch

from src.reader import (
    read_transactions_from_csv_file,
    read_transactions_from_excel_file,
)

data_csv = "id;state;date;amount\n650703;EXECUTED;2023-09-05T11:30:32Z;16210"
data_excel = "'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z'"


@patch("builtins.open", new_callable=mock_open, read_data=data_csv)
def test_read_transactions_from_csv_file(path):
    """Тест на чтение файла и возврат транзакций."""
    assert read_transactions_from_csv_file("p") == [
        {"id;state;date;amount": "650703;EXECUTED;2023-09-05T11:30:32Z;16210"}
    ]
    path.assert_called_with("p", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_transactions_from_csv_empty_file(path):
    """Тест на чтение пустого файла."""
    assert read_transactions_from_csv_file("p") == []
    path.assert_called_with("p", "r", encoding="utf-8")


def test_read_transactions_from_csv_file_not_found():
    """Тест на чтение файла, отcутствующего по указанному пути."""
    assert read_transactions_from_csv_file("p") == []


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
