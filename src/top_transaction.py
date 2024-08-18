from src.read_excel import read_excel

initial_list = read_excel("../data/operations.xlsx")


def top_five_transaction(my_list: list) -> list:
    """Функция для получения топ-5 транзакций по сумме платежа"""
    all_transactions = {}
    result = []

    for i in my_list:

        if i['Категория'] not in all_transactions and str(i['Сумма платежа'])[0:1] != "-":
            if i['Категория'] != "Пополнения":
                all_transactions[i['Категория']] = float(str(i['Сумма платежа'])[1:])

        elif (i['Категория'] in all_transactions and
              float(str(i['Сумма платежа'])[1:]) > all_transactions[i['Категория']]):

            all_transactions[i['Категория']] = float(str(i['Сумма платежа'])[1:])
    for i in my_list:
        for k, v in all_transactions.items():
            if k == i['Категория'] and v == float(str(i['Сумма платежа'])[1:]):
                result.append({
                    "date": i['Дата платежа'],
                    "amount": v,
                    "category": k,
                    "description": i['Описание']
                })

    return result



