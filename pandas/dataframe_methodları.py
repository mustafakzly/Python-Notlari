import pandas as pd
import numpy as np

data = {
        "column1":[1,2,3,4,5],
        "column2":[10,20,13,20,25],
        "column3":["abc","bcaa","ade","cb","dea"]
        }

df = pd.DataFrame(data)

def kareal(x):
    return x*x
kareal2 = lambda x: x * x 

result = df
result = df["column2"].unique()
result = df["column2"].nunique()
result = df["column2"].value_counts()
result = df["column1"] * 2
result = df["column1"].apply(kareal)
result = df["column1"].apply(kareal2)
result = df["column1"].apply(lambda x: x * x )
result = df["column3"].apply(len)
df["column4"] = df["column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("column2") # kolondaki sayıları sıralar
result = df.sort_values("column3")
result = df.sort_values("column3", ascending = False) # terse çevirme

data = {
        "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran"],
        "Kategori":["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap"],
        "Gelir": [20,30,15,14,32,42,12,36,52]
        }

df = pd.DataFrame(data)
print(df.pivot_table(index = "Ay", columns = "Kategori", values = "Gelir"))
print(result)