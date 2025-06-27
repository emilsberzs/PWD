import pandas as pd

pd.DataFrame

df = pd.read_csv("table.csv")
print(df.iloc[0:3])