import datetime


def greetings():
    time_obj = datetime.datetime.now()
    if 6 <= time_obj.hour <= 12:
        return 'Доброе утро'
    elif 13 <= time_obj.hour <= 18:
        return 'Добрый день'
    elif 19 <= time_obj.hour <= 23:
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'
