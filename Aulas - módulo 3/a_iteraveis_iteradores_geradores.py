import time
import sys

lista = [1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))  # é iterável (true)

lista1 = 123456
print(hasattr(lista1, '__iter__'))  # false

# para saber se o elemento é iterador(diferente de ser iterável).
print(hasattr(lista, '__next__'))  # false
lista = iter(lista)
print(hasattr(lista, '__next__'))  # true
print(next(lista))  # agora é iteravel e cada print mostrará o próximo valor
print(next(lista))
print(next(lista))

# este é um exemplo sem gerador, fazendo tudo de uma vez.
'''
def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()
for v in g:
    print(v)
'''


# agora é uma função geradora
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
print(g)  # está vendo um gerador

for v in g:
    print(v)

# veja que g é tanto iterável como iterador.
print(hasattr(g, '__next__'))  # true
print(hasattr(g, '__iter__'))  # true


# outro exemplo
def gera1():
    var = 'Valor 1'
    yield var
    var = 'Valor 2'
    yield var
    var = 'Valor 3'
    yield var


g1 = gera()
print(g1)
print(g1)
print(g1)

l1 = [x for x in range(1000)]
print(type(l1))  # type lista
l2 = (x for x in range(1000))  # apenas por usar parenteses já vira um gerador
print(type(l2))  # type generator

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
# muito menor em bytes por usar gerador mesmo se mudar o range para maior# ou
# menor só vai alterar o tamanho do consumo de memória na função que não
# utiliza gerador.
