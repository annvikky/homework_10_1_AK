import json
import logging
import os.path

path_to_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_list(path: str) -> list[dict]:
    """Получение списка с финансовыми транзакциями"""
    try:
        logger.info("Открываем json-файл")
        with open(path, "r", encoding="utf-8") as file:
            try:
                logger.info("Возвращаем транзакции из json-файла")
                transactions_list = json.load(file)
                return transactions_list
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка при распозновании json-файла: {ex}")
                transactions_list = []
                return transactions_list
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка при обнаружении json-файла: {ex}")
        transactions_list = []
        return transactions_list


# get_transactions_list(path_to_json)
