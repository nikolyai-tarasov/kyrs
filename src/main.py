from utils import (greetings, for_each_card, currency_rates,
                   top_five_transaction, get_price_stock)
from read_excel import read_excel
from views import filter_by_date
import json


def main(date: str, file_path: str, stocks: list):
    """Функция создающая JSON ответ для страницы главная"""
    my_list_trans = read_excel(file_path)
    filter_by_date(date, my_list_trans)
    greeting = greetings()
    cards = for_each_card(my_list_trans)
    top_trans = top_five_transaction(my_list_trans)
    stocks_prices = get_price_stock(stocks)

    date_json = json.dumps(
        {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_trans,
            "currency_rates": currency_rates,
            "stock_prices": stocks_prices,
        },
        indent=4,
        ensure_ascii=False,
    )
    return date_json


print(main("2021.11.12", "../data/operations.xlsx", ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]))
