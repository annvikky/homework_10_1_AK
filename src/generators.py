from typing import Any, Dict, Generator, List


def filter_by_currency(
    list_of_transactions: List[Dict[str, Any]], currency: str
) -> Generator:
    """Функция фильтрации по валюте, возвращает итератор"""
    if not list_of_transactions:
        print("Параметры заданы неверно")
    try:
        filtered_transactions = filter(
            lambda transaction: transaction.get("operationAmount")
            .get("currency")
            .get("code")
            == currency,
            list_of_transactions,
        )
        return filtered_transactions
    except Exception:
        print("Параметры заданы неверно")


def transaction_descriptions(list_of_transactions: List[Dict[str, Dict]]) -> Generator:
    """Функция-генератор для описания операций по очереди"""
    for transaction in list_of_transactions:
        yield transaction.get("description")


def card_number_generator(num_1: int, num_2: int) -> Generator:
    """Функция-генератор для вывода номера банковских карт"""
    if (isinstance(num_1, int) and isinstance(num_2, int)) is False:
        raise ValueError("Оба аргумента должны быть типом данных int")

    if num_1 < 1 or num_2 > 9999_9999_9999_9999:
        raise ValueError("Введен некорректный аргумент")

    if num_2 < num_1:
        raise ValueError("Второй аргумент не может быть меньше первого")

    for number in range(num_1, num_2 + 1):
        card_number = "0" * (16 - len(str(number))) + str(number)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
