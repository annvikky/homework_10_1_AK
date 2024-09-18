import json
import os.path

path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_transactions_list(path: str) -> list[dict]:
    """Получение списка с финансовыми транзакциями"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                transactions_list = json.load(file)
                return transactions_list
            except json.JSONDecodeError:
                transactions_list = []
                return transactions_list
    except FileNotFoundError:
        transactions_list = []
        return transactions_list


# print(get_transactions_list(path))
# print(path)
