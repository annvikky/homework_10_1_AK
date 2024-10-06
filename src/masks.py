import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..", "logs/masks.log"), mode="w"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(cart_number: str) -> str | None:
    """Возвращает маску номера карты в виде строки"""
    cart_number = str(cart_number)
    if cart_number.isdigit() and len(cart_number) == 16:
        logger.info("Получаем маску карты по правилу XXXX XX** **** XXXX")
        return f"{cart_number[:4]} {cart_number[4:6]} ** **** {cart_number[12:]}"
    else:
        logger.warning("Переданное значение не является числом и не содержит 16 знаков")
        return None


def get_mask_account(account_number: str) -> str | None:
    account_number = str(account_number)
    """Возвращает маску номера счета в виде строки"""
    if account_number.isdigit() and len(account_number) == 20:
        logger.info("Получаем маску счета по правилу **XXXX")
        return f"**{account_number[-4::]}"
    else:
        logger.warning("Переданное значение не является числом и не содержит 20 знаков")
        return None


# get_mask_card_number("123412312341234")
# get_mask_account("12345123451234512345")
