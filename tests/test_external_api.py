from unittest.mock import patch

from src.external_api import get_amount_in_rub


@patch("requests.request")
# создаем мок для получения результата запроса
def test_get_amount_in_rub(mock_request):
    """Тест на получение ответа по запросу."""
    mock_request.return_value.json.return_value = {"result": 7500.0}
    assert (
        get_amount_in_rub(
            {"operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}}}
        )
        == 7500.0
    )
