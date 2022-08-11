import pandas as pd

data = pd.read_csv("players.csv")
data.dropna(inplace = True)
print(data.columns)
#data["Player"] = data["Player"].str.upper()
#data["Player"] = data["Player"].str.lower()
#data["index"] = data["Player"].str.find("a")
#data = data[data.Player.str.contains("Jordan")]
#data = data.Player.str.replace(" ","-")
data[["firstName","LastName"]] = data["Player"].loc[data['Player'].str.split().str.len()==2].str.split(expand = True)
print(data)