import re
from collections import Counter
from typing import Generator


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


def counter_by_description(
    transactions_list: list[dict], category_list: list[dict | str]
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
