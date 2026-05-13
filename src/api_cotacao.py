import requests


def buscar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()

    cotacao = float(dados["USDBRL"]["bid"])

    return cotacao


def converter_dolar_para_real(valor_dolar):
    if valor_dolar <= 0:
        raise ValueError("O valor em dólar deve ser maior que zero.")

    cotacao = buscar_cotacao_dolar()

    return valor_dolar * cotacao