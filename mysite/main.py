import pandas as pd
import os
from polls.models import Room

def f(id, name):
    return str(id) + name


if __name__ == "__main__":
    df = pd.read_csv("\\".join([os.getcwd(), "tables", "{}.csv".format("room")]))
    fields = df.columns
    for i in df.index:
        values = df.loc[i, :]
        d = dict(list(zip(fields, values)))
        entry = Room(id=0, name="name")
