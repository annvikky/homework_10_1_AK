from src.widget import get_date, mask_account_card


def read_formatted_transaction(transaction: dict) -> str:
    # for el in transaction:
    try:
        formated_date = get_date(transaction["date"])
        description = transaction.get("description")

        if description == "Открытие вклада":
            way_to = mask_account_card(transaction.get("to"))
            transaction_info = way_to
        else:
            way_from = mask_account_card(transaction.get("from"))
            way_to = mask_account_card(transaction.get("to"))
            transaction_info = f"{way_from} -> {way_to}"
        amount = transaction.get(
            "amount", transaction.get("operationAmount", {}).get("amount")
        )
        currency = transaction.get(
            "currency_code",
            transaction.get("operationAmount", {}).get("currency", {}).get("code"),
        )
        return f"{formated_date} {description}\n{transaction_info}\nСумма: {amount} {currency}"
    except Exception as e:
        return f"Найдена некорректная транзакция. Ошибка: {e}"
