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


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)


def sort_by_date(
    list_transactions: List[Dict[str, str | int]], ascending: bool = True
) -> List[Dict]:
    """Функция сортировки по дате"""
    sorted_transactions = sorted(
        list_transactions, key=lambda d: d["date"], reverse=ascending
    )

    return sorted_transactions


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)
