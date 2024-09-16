import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")


def get_amount_in_rub(transaction: Any) -> float:
    """Функция для получения суммы транзакции с конвертацией в рубли, где необходимо."""
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            payload = {}
            headers = {"apikey": apikey}
            response = requests.request("GET", url, headers=headers, data=payload)
            amount = response.json()
            return amount["result"]
        else:
            return amount
    except KeyError:
        return 0


# transactions_list = (get_transactions_list(PATH))
# for transaction in transactions_list:
#     print(get_amount_in_rub(transaction))
