# Python project: Виджет банковских операций клиента

## Проект представляет собой приложение, позволяющее маскировать данные счета/карты клиента, сортировать операции по переданному ключу , сортировать операции по дате согласно заданному порядку. 
## Добавлен модуль с функциями фильтрации по валюте и ключу (описанию), генератор создания номера банковских карт в заданном диапазоне. 
## Добавлен декоратор для логирования начала и результата выполнения функции в консоль или заданный файл (при передаче параметра filename) 

## Установка:
1. Клонируйте репозиторий по SHH-ключу:
    ```
    git@github.com:annvikky/homework_10_1_AK.git
    ```
2. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
## Использование: 

При вводе конфиденциальной информации о номере расчетного счета или карты обеспечивается безопасный вывод данных в формате XXXX XX** **** XXXX/**XXXX через функции get_mask_card_number и get_mask_account.

При вводе списка операций доступна сортировка по статусу транзакции. Функция filter_by_state позволяет получить отсортированный список.

При вводе списка операций доступна сортировка по дате операции. Функция sort_by_date позволяет получить отсортированный список.

Доступна фильтрация данных о транзакциях по валюте при помощи функции-генератора filter_by_currency.

Доступна фильтрация данных о транзакциях по ключу description при помощи функции-генератора transaction_descriptions.

Посредством функции-генератора card_number_generator генерируются номера банковских карт в заданном диапазоне.

С помощью декоратора @log производится логирования начала и результата выполнения функции в консоль или заданный файл.


## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

## Тестирование:

Для всех вышеописанных функций и генераторов приведены unit-тесты. Покрытие тестами 100%.