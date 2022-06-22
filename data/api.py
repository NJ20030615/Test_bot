import sqlite3
import pandas as pd

def db_to_xlsx():
    conn = sqlite3.connect('data/main2.db')
    df = pd.read_sql_query("SELECT * FROM users", conn)
    df.to_excel('data/db.xlsx')
    conn.close()
