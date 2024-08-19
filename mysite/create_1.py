
import pandas as pd
import os
from django.db import connection

def insert_values(table):
    df = pd.read_csv("\\".join([os.getcwd(), "tables", "{}.csv".format(table)]))
    fields = ",".join(df.columns)
    values = ",\n".join([str(tuple(df.loc[i, :])) for i in df.index])
    return "INSERT INTO {} ({}) VALUES\n{}\n;".format(table, fields, values)

def executeSQL(commands):
    with connection.cursor() as cursor:
        for command in commands:
            print(command)
            cursor.execute(command)