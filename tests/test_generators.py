from typing import Dict, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
]


@pytest.mark.parametrize(
    "list_of_transactions, currency, filtered_transactions",
    [
        (transactions, "USD", usd_transactions),
        (transactions, "юань", []),
        ([], "USD", []),
    ],
)
def test_filter_by_currency(
    list_of_transactions: List[Dict[str, Dict]],
    currency: str,
    filtered_transactions: List[Dict[str, Dict]],
) -> None:
    # тест на корректность фильтрации
    assert (
        list(filter_by_currency(list_of_transactions, currency))
        == filtered_transactions
    )


def test_filter_by_currency_stop_iter() -> None:
    # тест на выбрасывание StopIteration при исчерпывании значений итератором
    with pytest.raises(StopIteration):
        output = filter_by_currency(transactions, "USD")
        for _ in range(4):
            next(output)


def test_filter_by_currency_with_raise() -> None:
    # тест на выбрасывание ошибки
    with pytest.raises(Exception):
        next(filter_by_currency(None, "USD"))


@pytest.mark.parametrize(
    "list_of_transactions, expected_descriptions",
    [
        (
            transactions,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        ([], []),
        ([{"id": 939719570}], [None]),
    ],
)
def test_transaction_descriptions(
    list_of_transactions: List[Dict[str, Dict]], expected_descriptions: List[str]
) -> None:
    # тест на корректность получения описаний по очереди
    descriptions = transaction_descriptions(list_of_transactions)
    assert list(descriptions) == expected_descriptions


@pytest.mark.parametrize(
    "num_1, num_2, expected_card_number",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999_9999_9999_9999, 9999_9999_9999_9999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(
    num_1: int, num_2: int, expected_card_number: str
) -> None:
    # тест на корректность получения номера карты
    assert list(card_number_generator(num_1, num_2)) == expected_card_number


@pytest.mark.parametrize("num_1, num_2", [(1, 0), (-1, 5), ("1", 3)])
def test_card_number_generator_with_raise(num_1: int, num_2: int) -> None:
    # тест на выбрасывание ошибок
    with pytest.raises(ValueError):
        list(card_number_generator(num_1, num_2))
