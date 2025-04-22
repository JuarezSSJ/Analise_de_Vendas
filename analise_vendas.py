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

#Qual foi o melhor mês de vendas? E o pior?
vendas_mes = base[["Ano-Mes","Vendedor","Valor Total"]]
vendas_mes = vendas_mes.groupby(["Ano-Mes"])[["Valor Total"]].sum().sort_values(by="Valor Total", ascending=False)
#print(vendas_mes)
#Melhor mês
base_melhor_mes = vendas_mes.iloc[0]
melhor_mes = vendas_mes.index[0]
valor_melhor_mes = base_melhor_mes["Valor Total"]
print(f"O mês com mais vendas foi: {melhor_mes} com o valor de R${valor_melhor_mes:,.2f}")

#Pior mês
base_pior_mes = vendas_mes.iloc[-1]
pior_mes = vendas_mes.index[-1]
valor_pior_mes = base_pior_mes["Valor Total"]
print(f"O mês com o pior resultado em vendas foi: {pior_mes} com o valor de R${valor_pior_mes:,.2f}")

#Quem são os melhores vendedores?
melhor_vendedor = base[["Ano-Mes","Vendedor","Valor Total"]]
melhor_vendedor = melhor_vendedor.groupby(["Vendedor"])[["Valor Total"]].sum().sort_values(by="Valor Total", ascending=False)

base_melhor_vendedor = melhor_vendedor.iloc[0]
nome_top_vendedor = melhor_vendedor.index[0]
valor_total_melhor_Vendedor = base_melhor_vendedor["Valor Total"]

print(f"O melhor vendedor(a) foi: {nome_top_vendedor} com o total de vendas R${valor_total_melhor_Vendedor:.2f}")