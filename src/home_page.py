
from src.greetings import greetings



def home_page(date: str):
    """Функция создающая JSON-ответ с данными 'Главная страница'"""
    greeting = greetings()
    list_by_date = []
    final_list = []
    year, month, day = int(date[0:4]), int(date[5:7]), int(date[8:10])

    # for i in initial_list:
    #     if i["Дата платежа"] == "nan" or type(i["Дата платежа"]) == float:
    #         continue
    #     elif date_start <= datetime.datetime.strptime(str(i["Сумма платежа"]),
    #                                                   '%d.%m.%Y') <= date_start + datetime.timedelta(
    #         days=90):
    #         list_by_date.append(i)
    # return final_list
    return year
