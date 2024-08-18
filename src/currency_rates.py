
import requests



def currency_rates():
    """Функция запроса курса валют"""
    url = f'https://v6.exchangerate-api.com/v6/9e32bad213767367e02af6fe/latest/USD'
    response_usd = requests.get(url)
    data_usd = response_usd.json()

    url = f'https://v6.exchangerate-api.com/v6/9e32bad213767367e02af6fe/latest/EUR'
    response_eur = requests.get(url)
    data_eur = response_eur.json()

    result = [{"currency": "USD",
               "rate": round(data_usd["conversion_rates"]["RUB"], 2)},
              {"currency": "EUR",
               "rate": round(data_eur["conversion_rates"]["RUB"], 2)}]
    return result
