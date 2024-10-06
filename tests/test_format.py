import pytest

from src.format import read_formatted_transaction

first = {
    "id": 634356296,
    "state": "EXECUTED",
    "date": "2018-01-21T01:10:28.317704",
    "operationAmount": {
        "amount": "96900.92",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 33407225454123927865",
    "to": "Счет 79619011266276091215",
}

second = {
    "id": 634356296,
    "state": "EXECUTED",
    "date": "2018-01-21T01:10:28.317704",
    "amount": 96900.92,
    "currency_name": "руб.",
    "currency_code": "RUB",
    "description": "Перевод со счета на счет",
    "from": "Счет 33407225454123927865",
    "to": "Счет 79619011266276091215",
}

result = """01.21.2018 Перевод со счета на счет
Счет **7865 -> Счет **1215
Сумма: 96900.92 RUB"""


@pytest.mark.parametrize("transaction", [first, second])
def test_read_formatted_transaction(transaction):
    """Тест на корректность работы функции."""
    assert read_formatted_transaction(transaction) == result


def test_read_formatted_transaction_with_exception():
    """Тест на корректность работы функции при ошибке"""
    assert read_formatted_transaction({}).startswith("Найдена некорректная")
