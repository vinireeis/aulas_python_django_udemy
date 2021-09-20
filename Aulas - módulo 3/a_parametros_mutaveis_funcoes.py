# objetos mutáveis, ex listas e dicionários
# imutaveis, tuplas, strings, números, true, false, None etc.

def lista_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)
