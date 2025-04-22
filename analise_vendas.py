import pandas as pd

#importando base
base = pd.read_csv("vendas.csv")

base.head()

#convertendo coluna Data em datatime

base["Data"] = pd.to_datetime(base["Data"])

base["Ano-Mes"] = base["Data"].dt.to_period("M")

base.dtypes

#Qual foi o total de vendas em um determinado período?

#Setembro
vendas_set_24 = base[["Ano-Mes", "Produto", "Quantidade", "Preço Unitário", "Valor Total"]]
vendas_set_24 = vendas_set_24.groupby(["Ano-Mes", "Produto"])[["Quantidade", "Preço Unitário", "Valor Total"]].sum().reset_index()
vendas_set_24 = vendas_set_24[(vendas_set_24["Ano-Mes"] == "2024-09")].sort_values(by = "Valor Total", ascending=False)
vendas_set_24

#Produto que foi mais vendido
#vendas_set_24.info()
prod_mais_vend_set_24 = vendas_set_24.iloc[0]
prod_mais_vend_set_24

#Produto que teve um maior valor total no acumulado do mês: Notbook

#Qual o ticket médio das vendas?

tkm = base[["Produto", "Quantidade", "Valor Total"]]
tkm = tkm.groupby(["Produto"])[["Quantidade", "Valor Total"]].sum().reset_index()
tkm["Tkm"] = tkm["Valor Total"]/tkm["Quantidade"]
tkm.sort_values(by="Tkm", ascending=False)

#produto com maior Tkm
tkm.sort_values(by="Tkm", ascending=False).iloc[0].loc["Produto"]

#Quais são os produtos mais vendidos? - reutilizando o df tkm

mais_vendidos = tkm.sort_values(by= "Quantidade", ascending=False)
mais_vendidos[["Produto","Quantidade"]].head(3) #3 produtos mais vendidos