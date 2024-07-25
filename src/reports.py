from turtle import pd
from typing import Optional, List, Any
import datetime
import pandas as pd
from src.read_excel import read_excel


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> list[Any]:
    list_by_category = []
    fin_list = []
    date_time = datetime.datetime.now()
    month_now = date_time.month
    date_time_str_now = date_time.strftime("%d-%m-%Y")

    if date is None:
        for i in transactions:
            if i["Категория"] == category:
                list_by_category.append(i)
    return list_by_category


df = read_excel("../data/operations.xlsx")
if __name__ == "__main__":
    print(spending_by_category(df, "Красота"))
