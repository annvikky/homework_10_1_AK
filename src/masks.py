def get_mask_card_number(cart_number: str) -> str | None:
    """Возвращает маску номера карты в виде строки"""
    cart_number = str(cart_number)
    if cart_number.isdigit() and len(cart_number) == 16:
        return f"{cart_number[:4]} {cart_number[4:6]} ** **** {cart_number[12:]}"
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    account_number = str(account_number)
    """Возвращает маску номера счета в виде строки"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4::]}"
    else:
        return None
