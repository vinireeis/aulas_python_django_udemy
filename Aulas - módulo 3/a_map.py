from a_dados import produtos, lista, pessoas

nova_lista = map(lambda x: x * 2, lista)  # mapeando a lista
print(lista)
print(list(nova_lista))

new_lista = [x * 2 for x in lista]  # resolvendo com list comprehensions
print(new_lista)

for produto in produtos:
    print(produto)

precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)  # funcao para aumentar preco
    return p

novos_precos = map(aumenta_preco, produtos)  # calculando novo preco
for p in novos_precos:
    (print(p))

nomes = map(lambda p: p['nome'], pessoas)
print(list(nomes))