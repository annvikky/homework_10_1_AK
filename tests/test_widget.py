import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    # тест на корректность распознавания типа входных данных и применения соответствующей маскировки
    assert (
        mask_account_card("Visa Platinum 8990922113665229")
        == "Visa Platinum 8990 92 ** **** 5229"
    )

    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"


@pytest.mark.parametrize(
    "payment_details, expected_details",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92 ** **** 5229"),
        ("Maestro 1596837868705199", "Maestro 1596 83 ** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98 ** **** 7658"),
    ],
)
def test_mask_account_card_as_expected(payment_details, expected_details):
    # тест на проверку универсальности функции
    assert mask_account_card(payment_details) == expected_details


@pytest.mark.parametrize(
    "payment_details, expected_details",
    [
        ("Union Pay 8990922113665229", None)
        or ("", None)
        or ("Visa Platinum 899092211366522", None)
        or ("VisaPlatinum899092211366522", None)
        or ("Счет 3538303347444789556", None)
        or ("Счет35383033474447895560", None)
    ],
)
def test_mask_account_card_invalid_number(payment_details, expected_details):
    assert mask_account_card(payment_details) is expected_details


@pytest.mark.parametrize(
    "date_info, expected_date_format",
    [
        ("2024-03-11T02:26:18.671407", "03.11.2024"),
        ("2024-05-11T02:26:18.671407", "05.11.2024"),
    ],
)
def test_get_date_as_expected(date_info, expected_date_format):
    # тест на правильность преобразование даты
    assert get_date(date_info) == expected_date_format


def test_get_data_wrong_value():
    # тест на ошибку в занчении даты
    with pytest.raises(ValueError):
        get_date("2024-13-11T02:26:18.671407")
