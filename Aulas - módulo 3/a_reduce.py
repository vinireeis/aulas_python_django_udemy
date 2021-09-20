from functools import reduce
from a_dados import pessoas, lista, produtos

acumula = 0
for item in lista:
    acumula += item
print(acumula)
# vamos fazer a mesma coisa com a funcao reduce


soma_lista = reduce(lambda ac, item: item + ac, lista, 0)
# ac = acumulador ou contador
# item = cada item da lista ( for x in lista)
# vai somar cada item ao acumulador
# recebe a lista como parametro
# inicia o acumulador com valor 0

print(soma_lista)

soma_precos1 = reduce(lambda ac, produto: produto['preco'] + ac, produtos, 0)
print(round(soma_precos1, 2))  # arredondado para 2 casas.

print(round(soma_precos1/len(produtos), 2)) # media de precos produtos

soma_idades = reduce(lambda ac, pessoa: pessoa['idade'] + ac, pessoas, 0)
print(soma_idades)  # total de idade
print(soma_idades/len(pessoas))  # media de idade

