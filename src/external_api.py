import os
from typing import Any

from dotenv import load_dotenv

from src.utils import get_transactions_list, PATH

import requests

load_dotenv()
apikey = os.getenv("API_KEY")


def get_amount(transaction: Any) -> float:
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        payload = {}
        headers = {"apikey": apikey}
        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        return result["result"]
    else:
        return amount


transactions_list = (get_transactions_list(PATH))
for transaction in transactions_list:
    print(get_amount(transaction))
