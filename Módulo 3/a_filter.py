from a_dados import pessoas, lista, produtos

nova_lista = filter(lambda x: x > 5, lista)  # filter
print(list(nova_lista))

new_lista = [x for x in lista if x > 5]  # list comprehensions
print(new_lista)

nova_lista1 = filter(lambda p: p['preco'] > 50, produtos)  # filter
print(list(nova_lista1))  # produtos onde o preço é maior que 50, gerando nova lista

def filtra(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False
# vantagem de trabalhar com funcoes é poder reutilizar a funcao em outro loca, diferente do lambda
print('abaixo é com a funcao')
nova_lista2 = filter(filtra, produtos)
print(list(nova_lista2))
