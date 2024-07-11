from typing import Any


def filter_by_state(
    list_of_transactions: list[dict[str, str | int]],
    state_transaction: str = "EXECUTED",
) -> Any:
    """Функция сортировки по статусу"""
    executed_list = []
    cancelled_list = []
    for key in list_of_transactions:
        if key.get("state") == state_transaction:
            executed_list.append(key)
        else:
            cancelled_list.append(key)
    return f"{executed_list}, \n{cancelled_list}"


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


def sort_by_date(list_of_transactions: list[dict[str, str | int]]) -> Any:
    """Функция сортировки по дате"""
    sorted_list = sorted(list_of_transactions, key=lambda d: d["date"], reverse=True)

    return sorted_list


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
