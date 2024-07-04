def get_mask_card_number(cart_number: str) -> str | None:
    """Возвращает маску номера карты в виде строки"""
    if cart_number.isdigit() and len(cart_number) == 16:
        return f"{cart_number[:4]} {cart_number[4:6]} ** **** {cart_number[12:]}"
    else:
        return None


if __name__ == "__main__":
    print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(account_number: str) -> str | None:
    """Возвращает маску номера счета в виде строки"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4::]}"
    else:
        return None


if __name__ == "__main__":
    print(get_mask_account(str(73654108430135874305)))
