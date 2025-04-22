import pandas as pd

#importando base
base = pd.read_csv("vendas.csv")

base.head()

#convertendo coluna Data em datatime

base["Data"] = pd.to_datetime(base["Data"])

base["Ano-Mes"] = base["Data"].dt.to_period("M")

base.dtypes
