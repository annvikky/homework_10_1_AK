from src.filter import counter_by_description, filter_by_search_string
from src.format import read_formatted_transaction
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reader import (path_to_file_csv, path_to_file_xls, read_transactions_from_csv_file,
                        read_transactions_from_excel_file)
from src.utils import get_transactions_list, path_to_json


def main():
    """ Запуск программы."""
    user_transaction_list = []

    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )
    number = input("Введите число: ")

    while not isinstance(number, int) and int(number) not in [1, 2, 3]:
        print(f"Вы ввели '{number}'. Это некорректное число. Попробуйте еще раз!")
        number = input("Введите число: ")
    number = int(number)

    if number == 1:
        user_transaction_list = get_transactions_list(path_to_json)
        print("Для обработки выбран JSON-файл\n")
    elif number == 2:
        user_transaction_list = read_transactions_from_csv_file(path=path_to_file_csv)
        print("Для обработки выбран CSV-файл\n")
    elif number == 3:
        user_transaction_list = read_transactions_from_excel_file(path=path_to_file_xls)
        print("Для обработки выбран XLSX-файл\n")

    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
"""
    )

    state = input().upper()
    while state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(
            f"""Статус операции {state} недоступен.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """
        )
        state = str(input("Введите статус: "))

    user_transaction_list = filter_by_state(user_transaction_list, state)

    print(f"\nОперации отфильтрованы по статусу {state}")

    print("Отсортировать операции по дате? Да/Нет")

    user_sorted_by_date = input().upper()

    if user_sorted_by_date == "ДА":
        print("Отсортировать по возрастанию или по убыванию?")
        text = input()
        if "возр" in text:
            user_transaction_list = sort_by_date(user_transaction_list, False)

        else:
            user_transaction_list = sort_by_date(user_transaction_list, True)

    print("Выводить только рублевые тразакции? Да/Нет")

    user_sorted_by_currency = input().upper()

    if user_sorted_by_currency == "ДА":
        user_transaction_list = list(filter_by_currency(user_transaction_list, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    user_filtered_by_search_string = input().upper()

    if user_filtered_by_search_string == "ДА":
        search_string = input("Введите слово для поиска: ")
        user_transaction_list = list(
            filter_by_search_string(user_transaction_list, search_string)
        )

    print("Распечатываю итоговый список транзакций...")
    user_category_list = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]
    counter_by_description(user_transaction_list, category_list=user_category_list)

    user_transaction_list_count = len(user_transaction_list)
    if user_transaction_list_count == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {user_transaction_list_count}")
        for transaction in user_transaction_list:
            formatted_transaction = read_formatted_transaction(transaction)
            print(f"{formatted_transaction}\n")


main()
