from collections import Counter
from typing import Dict, List

import pytest

from src.filter import counter_by_description, filter_by_search_string

transactions = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Оплата организации",
    },
]


@pytest.fixture()
def filter_by_search_string_corrected_work() -> List[Dict]:
    return [
        {
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
    ]


def test_filter_by_search_string(
    filter_by_search_string_corrected_work: List[Dict],
) -> None:
    """Тест на корректность фильтрации."""
    assert list(filter_by_search_string(transactions, search_string="пере")) == [
        {
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
    ]


def test_filter_by_search_string_without_value() -> None:
    """Тест на корректность работы функции при условии отсутствия ключа."""
    assert (
        list(
            filter_by_search_string(
                [{"id": 650703.0, "state": "EXECUTED"}], search_string="пере"
            )
        )
        == []
    )


def test_filter_by_search_string_wrong_search_string() -> None:
    """Тест на корректность работы функции при некорректном запросе."""
    assert list(filter_by_search_string(transactions, search_string="gtht")) == []


# @pytest.fixture()
# def counter_by_description_correct_work() -> List[Dict]:
#     return [Counter({'Перевод организации': 1})]


# def test_counter_by_description(counter_by_description_correct_work: List[Dict]) -> None:
#     """ Тест на корректность подсчета вхождений заданных категорий."""
#     assert counter_by_description(transactions, ['Перевод организации', 'Перевод с карты на карту']) == [
#         Counter({'Перевод организации': 1})]


@pytest.mark.parametrize(
    "list_of_transactions, category_list, counted_transactions",
    [
        (
            transactions,
            ["Перевод организации", "Перевод с карты на карту"],
            [Counter({"Перевод организации": 1})],
        ),
        (transactions, ["Что-то"], [Counter()]),
        ([], ["Перевод организации", "Перевод с карты на карту"], [Counter()]),
    ],
)
def test_counter_by_description_for_absent_category(
    list_of_transactions, category_list, counted_transactions
) -> None:
    """Тест на корректную работу функции с учетом пустого списка транзакций и отсутствие категорий для выборки."""
    assert (
        counter_by_description(list_of_transactions, category_list)
        == counted_transactions
    )
