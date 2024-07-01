
import psycopg2
import pandas as pd
con = psycopg2.connect(database="postgres", user="postgres", password="12345678", host='127.0.0.1', port='5432')

cur = con.cursor()
query = "SELECT author, title, amount, price from book2"
df = pd.read_sql(query, con)
print(df)