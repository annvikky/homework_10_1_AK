from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date

test_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
sorted_list_by_state_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
sorted_list_by_state_2 = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
sorted_list_by_date_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
sorted_list_by_date_2 = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.mark.parametrize(
    "list_transactions, state_transaction, filtered_transactions",
    [
        (test_list, None, sorted_list_by_state_1),
        (test_list, "EXECUTED", sorted_list_by_state_1),
        (test_list, "CANCELED", sorted_list_by_state_2),
        (test_list, "CANSELED", []),
        ([], None, []),
    ],
)
def test_filter_by_state(
    list_transactions: List[Dict[str, str | int]],
    state_transaction: str,
    filtered_transactions: List[Dict],
) -> None:
    # тест фильтрации списка по заданному статусу "state"
    if state_transaction is None:
        assert filter_by_state(list_transactions) == filtered_transactions
    else:
        assert (
            filter_by_state(list_transactions, state_transaction)
            == filtered_transactions
        )


@pytest.mark.parametrize(
    "list_transactions, descending, sorted_transactions",
    [
        (test_list, None, sorted_list_by_date_1),
        (test_list, False, sorted_list_by_date_2),
        (test_list, True, sorted_list_by_date_1),
    ],
)
def test_sort_by_date(
    list_transactions: List[Dict[str, str | int]],
    descending: bool,
    sorted_transactions: List[Dict],
) -> None:
    # тест на корректность сортировки по дате
    if descending is None:
        assert sort_by_date(list_transactions) == sorted_transactions
    else:
        assert sort_by_date(list_transactions, descending) == sorted_transactions


@pytest.fixture
def sort_by_date_same_date() -> List[Dict]:
    return [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_date(sort_by_date_same_date: List[Dict]) -> None:
    # тест на сортировку списка с одинаковыми датами
    assert sort_by_date(sort_by_date_same_date) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sort_by_date_incorrect_date() -> List[Dict]:
    return [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "23-03-2021T18:35:29.512364"},
        {"date": "a"},
        {"date": "2020-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_incorrect_date(sort_by_date_incorrect_date: List[Dict]) -> None:
    # тест на сортировку списка с некорректными датами
    assert sort_by_date(sort_by_date_incorrect_date) == [
        {"date": "a"},
        {"date": "23-03-2021T18:35:29.512364"},
        {"date": "2020-07-03T18:35:29.512364"},
        {"date": "2019-07-03T18:35:29.512364"},
    ]
