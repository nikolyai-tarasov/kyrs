from src.read_excel import read_excel


initial_list = read_excel("../data/operations.xlsx")


def for_each_card(my_list: list) -> list:
    """Функция создания информации по каждой карте"""
    cards = {}
    result = []
    for i in my_list:
        if i['Номер карты'] == 'nan' or type(i['Номер карты']) == float:
            continue
        elif i['Сумма платежа'] == 'nan':
            continue
        else:
            if i['Номер карты'][1:] in cards:
                cards[i['Номер карты'][1:]] += float(str(i['Сумма платежа'])[1:])
            else:
                cards[i['Номер карты'][1:]] = float(str(i['Сумма платежа'])[1:])
    for k, v in cards.items():
        result.append({"last_digits": k,
                       "total_spent": round(v, 2),
                       "cashback": round(v / 100, 2)})
    return result



