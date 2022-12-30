import pandas as pd
import sqlite3


def create_table():
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    df = pd.read_csv("converted_dataframe.csv")
    df.to_sql('exchange_rates', sqlite_connection, if_exists='replace', index=False)
    cursor.close()


create_table()