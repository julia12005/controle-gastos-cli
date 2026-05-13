from unittest.mock import Mock, patch

from src.api_cotacao import buscar_cotacao_dolar, converter_dolar_para_real


@patch("src.api_cotacao.requests.get")
def test_buscar_cotacao_dolar_com_api_mockada(mock_get):
    resposta_mock = Mock()
    resposta_mock.json.return_value = {
        "USDBRL": {
            "bid": "5.20"
        }
    }
    resposta_mock.raise_for_status.return_value = None
    mock_get.return_value = resposta_mock

    cotacao = buscar_cotacao_dolar()

    assert cotacao == 5.20
    mock_get.assert_called_once()


@patch("src.api_cotacao.buscar_cotacao_dolar")
def test_converter_dolar_para_real(mock_buscar_cotacao):
    mock_buscar_cotacao.return_value = 5.20

    resultado = converter_dolar_para_real(10)

    assert resultado == 52.0