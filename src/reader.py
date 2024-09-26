import csv
import logging
import os.path

import pandas as pd

path_to_file_csv = os.path.join(os.path.dirname(__file__), "..", "transactions.csv")
path_to_file_xls = os.path.join(
    os.path.dirname(__file__), "..", "transactions_excel.xlsx"
)

logger = logging.getLogger("reader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/reader.log", mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_from_csv_file(path: str) -> list[dict]:
    """Чтение csv-файла и вывод списка транзакций."""
    logger.info("Открываем csv-файл")
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                logger.info("Возвращаем транзакции из csv-файла")
                reader = csv.DictReader(file)
                df = pd.DataFrame(reader)
                df_dict = df.to_dict(orient="records")
                return df_dict
            except pd.errors.EmptyDataError as ex:
                logger.warning(f"Файл пустой: {ex}")
                return []

    except FileNotFoundError:
        logger.error(f"Файл по пути {path} не найден.")
        return []


# read_transactions_from_csv_file(path=path_to_file_csv)


def read_transactions_from_excel_file(path: str) -> list[dict]:
    """Чтение excel-файла и вывод списка транзакций."""
    logger.info("Открываем xls-файл")

    try:
        try:
            logger.info("Возвращаем транзакции из xls-файла")
            excel_data = pd.read_excel(path)
            excel_dict = excel_data.to_dict(orient="records")
            return excel_dict
        except pd.errors.EmptyDataError as ex:
            logger.warning(f"Файл пустой: {ex}")
            return []

    except FileNotFoundError:
        logger.error(f"Файл по пути {path} не найден.")
        return []


# read_transactions_from_excel_file(path=path_to_file_xls)
