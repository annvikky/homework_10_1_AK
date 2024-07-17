from typing import Dict, List


def filter_by_state(
    list_transactions: List[Dict[str, str | int]],
    state_transaction: str = "EXECUTED",
) -> List[Dict]:
    """Функция сортировки по статусу"""
    filtered_transactions = []
    for key in list_transactions:
        if key.get("state") == state_transaction:
            filtered_transactions.append(key)

    return filtered_transactions


def sort_by_date(
    list_transactions: List[Dict[str, str | int]], descending: bool = True
) -> List[Dict]:
    """Функция сортировки по дате"""
    sorted_transactions = sorted(
        list_transactions, key=lambda d: d["date"], reverse=descending
    )

    return sorted_transactions
