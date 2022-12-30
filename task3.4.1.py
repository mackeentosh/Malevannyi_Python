import pandas as pd
import math


def convert_currency(string, df_currency):
    if pd.isnull(string):
        return string
    arr = string.split()
    if df_currency.columns.__contains__(arr[1]):
        date = arr[2]
        course = df_currency[df_currency["date"] == date[:7]][arr[1]].values
        if not math.isnan(course[0]):
            return round(float(arr[0]) * course[0])
    return arr[0]


def convert_currencies_in_file():
    file_name = "vacancies_dif_currencies.csv"
    file_currencies = "currencies_years.csv"
    dataframe = pd.read_csv(file_name)
    dataframe_curr = pd.read_csv(file_currencies)
    dataframe.insert(1, "salary", None)
    dataframe.assign(salary=lambda x: x.salary_from)
    dataframe["salary"] = dataframe[["salary_from", "salary_to"]].mean(axis=1)
    dataframe["salary"] = dataframe["salary"].astype(str) + " " + + dataframe["salary_currency"] + " " + dataframe["published_at"]
    dataframe["salary"] = dataframe["salary"].apply(lambda x: convert_currency(x, dataframe_curr))
    dataframe = dataframe.drop(columns=['salary_from', 'salary_to', 'salary_currency'])
    dataframe.head(100).to_csv("converted_dataframe.csv", index=False)


convert_currencies_in_file()