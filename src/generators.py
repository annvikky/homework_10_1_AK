from typing import List, Dict, Generator


def filter_by_currency(
    list_of_transactions: List[Dict[str, Dict]], currency: str
) -> Generator:
    """Функция фильтрации по валюте, возвращает итератор"""
    if not list_of_transactions:
        print("Параметры заданы не верно")
    try:
        filtered_transactions = list(
            filter(
                lambda transaction: transaction.get("operationAmount")
                .get("currency")
                .get("code")
                == currency,
                list_of_transactions,
            )
        )
        yield filtered_transactions
    except Exception:
        print("Параметры заданы не верно")
