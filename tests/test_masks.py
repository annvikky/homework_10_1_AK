from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    # тест на корректность маскировки карты
    assert get_mask_card_number("7000792289606361") == "7000 79 ** **** 6361"
    # тест на корректность маскировки карты при неверной длине номера карты
    assert get_mask_card_number("700079228960636") is None

    assert get_mask_card_number("70007922896063611") is None
    # тест на корректность маскировки карты при передаче пустой строки
    assert get_mask_card_number("") is None
    # тест на корректность маскировки карты при неверной передаче номера карты
    assert get_mask_card_number("не помню номер карты") is None


def test_get_mask_account() -> None:
    # тест на корректность маскировки счета
    assert get_mask_account("73654108430135874305") == "**4305"

    # тест на корректность маскировки счета при неверной длине номера счета
    assert get_mask_account("7365410843013587430") is None

    assert get_mask_account("736541084301358743055") is None
    # тест на корректность маскировки счета при передаче пустой строки
    assert get_mask_account("") is None
    # тест на корректность маскировки счета при неверной передаче номера счета
    assert get_mask_account("не помню номер счета") is None
