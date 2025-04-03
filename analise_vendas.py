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

#ordenar do maior para o menor para pegar os 5 produtos que mais venderam
top_vendas = resumo_vendas.sort_values(ascending=False).head(5)
top_vendas

#ordenar do menor para o maior para pegar os 5 produtos que menos venderam
menos_vendas = resumo_vendas.sort_values(ascending=True).head(5)
menos_vendas

#produto x venda total
venda_prod = vendas[["Produto","Valor Total"]]
vendas_prod = venda_prod.groupby("Produto")["Valor Total"].sum()
vendas_prod.sort_values(ascending=False).head(5)

#convertendo a coluna Data em datatime
vendas["Data"] = pd.to_datetime(vendas["Data"])
#cria coluna no final Ano-Mes
vendas["Ano-Mes"] = vendas["Data"].dt.to_period("M")
#Criei a coluna ano para ajudar nos filtros
vendas["Ano"] = vendas['Data'].dt.year
vendas.head()

#Total de vendas por mês
vendas_por_mes = vendas[["Ano-Mes", "Valor Total"]]
vendas_por_mes = vendas.groupby("Ano-Mes")["Valor Total"].sum()
vendas_por_mes

#produtos , quantidades, valor total

prod_quat_valortotal = vendas[["Ano-Mes" ,"Produto", "Quantidade", "Valor Total"]]
prod_quat_valortotal = prod_quat_valortotal.groupby("Produto")[["Quantidade", "Valor Total"]].sum()
prod_quat_valortotal = prod_quat_valortotal.sort_values(by="Valor Total" , ascending=False)
prod_quat_valortotal["Valor Unid Med"] = prod_quat_valortotal["Valor Total"] / prod_quat_valortotal["Quantidade"]
prod_quat_valortotal

tkm_tri_2025 = vendas[["Ano-Mes","Produto","Valor Total"]]
tkm_tri_2025 = tkm_tri_2025.groupby(["Ano-Mes","Produto"])["Valor Total"].sum().reset_index()
tkm_tri_2025 = tkm_tri_2025[(tkm_tri_2025["Ano-Mes"] >= "2025-01") & (tkm_tri_2025["Ano-Mes"] <= "2025-03")]
tkm_tri_2025.sort_values(by = ["Ano-Mes","Valor Total"], ascending = [True,False])


#loop para avaliar o trimestre dos produtos mais vendidos 
for i in top_vendas.index:
    prod_ava_trimestre = tkm_tri_2025[tkm_tri_2025["Produto"] == i]
    print(prod_ava_trimestre)

#agrupei as vendas do trimestre 25 por produto e ordenei do maior para o menor, com isso posso avaliar o desempenho seguindo por valor total de venda
top_vendas_tri25 = tkm_tri_2025.groupby("Produto")["Valor Total"].sum().sort_values(ascending=False).reset_index().head(5)
top_vendas_tri25
for i in top_vendas_tri25["Produto"]:
    prod_ava_trimestre = tkm_tri_2025[tkm_tri_2025["Produto"] == i]
    print(prod_ava_trimestre)

#Comparativo 4 quartil de 24 x 1 Quartil 25
vendas_por_produto_total = vendas[["Ano-Mes","Produto", "Quantidade", "Valor Total"]]
#vendas_por_produto_total
quarto_tri_24 = vendas_por_produto_total[(vendas_por_produto_total["Ano-Mes"] >= "2024-10") & (vendas_por_produto_total["Ano-Mes"] <= "2024-12")]
#produto mais vendido no 4tri24
prod_mais_vend_4tri24 = quarto_tri_24.groupby("Produto")[["Quantidade", "Valor Total"]].sum().reset_index()
prod_mais_vend_4tri24.sort_values(by = "Quantidade", ascending=False).loc[0]
print(prod_mais_vend_4tri24['Valor Total'].loc[0]/(quarto_tri_24["Valor Total"].sum())*100)
#quarto_tri_24 = quarto_tri_24.groupby([])

#Primeiro Tri de 25 - filtro e agrupar
primeiro_tri_25 = vendas_por_produto_total[(vendas_por_produto_total["Ano-Mes"] >= "2025-01") & (vendas_por_produto_total["Ano-Mes"] <= "2025-03")]
prod_mais_vend_1tri25 = primeiro_tri_25.groupby("Produto")[["Quantidade", "Valor Total"]].sum().reset_index()
prod_mais_vend_1tri25.sort_values(by = "Quantidade", ascending=False).loc[0]
#print(primeiro_tri_25)