import pandas as pd
import datetime as dt
import lxml


def read_csv_and_get_currency_frequency(file):
    pd.set_option("expand_frame_repr", False)
    df = pd.read_csv(file)
    df_currency = df.groupby("salary_currency")["name"].agg(["count"])
    df_currency.reset_index(inplace=True)
    df_currency = df_currency.sort_values("count", ascending=False)
    print(df_currency)


def get_currencies_list(columns):
    array = []
    for year in range(2003, 2023):
        for month in range(1, 13):
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month:02}/{year}"
            df = pd.read_xml(url, encoding="cp1251")[["CharCode", "Nominal", "Value"]]
            df = df[df["CharCode"].isin(columns)]
            df["Value"] = df["Value"].apply(lambda f: float(f.replace(",", ".")))
            currencies = pd.concat([pd.Series([f"{year}-{month:02}"]), round(df["Value"] / df["Nominal"], 7)])
            array.append((list(currencies)))
    return array


columns_names = ["date", "BYR", "USD", "EUR", "KZT", "UAH"]

read_csv_and_get_currency_frequency("vacancies_dif_currencies.csv")
result = get_currencies_list(columns_names)

result_file = pd.DataFrame(result)
result_file.columns = columns_names
result_file.to_csv("currencies_years.csv", index=False)