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

