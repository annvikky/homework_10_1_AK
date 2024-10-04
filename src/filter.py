import re
from collections import Counter
from typing import Any, List, Generator

from src.reader import (
    path_to_file_csv,
    path_to_file_xls,
    read_transactions_from_csv_file,
    read_transactions_from_excel_file,
)
from src.utils import get_transactions_list, path_to_json


def filter_by_search_string(
    transactions_list: list[dict], search_string: str
) -> Generator:
    """Фильтрация списка транзауций по поисковому слову."""
    for transaction in transactions_list:
        description = transaction.get("description")
        if description:
            result = re.findall(search_string, str(description), flags=re.IGNORECASE)
            if result:
                yield transaction


# print(list(filter_by_search_string(transactions_list=read_transactions_from_excel_file(path_to_file_xls), search_string="пере")))
# print(list(filter_by_search_string(transactions_list=read_transactions_from_csv_file(path_to_file_csv), search_string="пере")))
# print(list(filter_by_search_string(transactions_list=get_transactions_list(path_to_json), search_string="пере")))


def counter_by_description(
    transactions_list: list[dict], category_list: list[dict]
) -> list:
    """Подсчет количества операций категории."""
    list_of_descriptions = []
    for transaction in transactions_list:
        description = transaction.get("description")
        if description:
            for category in category_list:
                if category == description:
                    list_of_descriptions.append(description)
    counted_descriptions = Counter(list_of_descriptions)
    return [counted_descriptions]


# print(counter_by_description(read_transactions_from_csv_file(path_to_file_csv), ["Перевод организации", "Перевод с карты на карту", "Что-то"]))
# print(counter_by_description(get_transactions_list(path_to_json), ["Перевод организации", "Перевод с карты на карту", "Что-то"]))
# print(counter_by_description(read_transactions_from_excel_file(path_to_file_xls), ["Перевод организации", "Перевод с карты на карту", "Что-то"]))
# print(counter_by_description([], ["Перевод организации", "Перевод с карты на карту", "Что-то"]))
