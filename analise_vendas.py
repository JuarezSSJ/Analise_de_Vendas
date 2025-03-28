import pandas as pd

#importando base
vendas = pd.read_csv("vendas.csv")

vendas

#verifica o tipo dos objetos das colunas
vendas.dtypes

#resumo tecnico onde tem as colunas, quantidade de linhas e o tipo
vendas.info()

#separando somente a coluna produto
column_specific = vendas["Produto"]
column_specific.head()

#to_string() serve para visualizar toda a tabela
print(vendas.to_string())

#data correlations

vendas.corr()#metodo vai ignonar colunas não numericas

#estudando Replacing 
print(vendas)
new_df_teste = vendas
new_df_teste.loc[1,"Quantidade"] = 3

#Produtos mais vendidos
prod_mais_vendidos = vendas[["Produto","Quantidade"]]
resumo_vendas = prod_mais_vendidos.groupby("Produto")["Quantidade"].sum()
resumo_vendas = resumo_vendas.sort_values(ascending=False)
resumo_vendas