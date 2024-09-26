import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions_list

data = '{"data": "2024/01/01"}'


@patch("builtins.open", new_callable=mock_open, read_data=data)
def test_get_transactions_list(path):
    """Тест на чтение файла и возврат содержимого в json."""
    assert get_transactions_list("p") == json.loads(data)
    path.assert_called_with("p", "r", encoding="utf-8")


def test_get_transactions_list_not_found():
    """Тест на чтение файла, отcутствующего по указанному пути."""
    assert get_transactions_list("p") == []


@patch("builtins.open", new_callable=mock_open, read_data='{"data": 2024/01/01}')
def test_get_transactions_list_invalid_json(path):
    """Тест на чтение некорректного формата json-файла."""
    assert get_transactions_list("p") == []
    path.assert_called_with("p", "r", encoding="utf-8")
