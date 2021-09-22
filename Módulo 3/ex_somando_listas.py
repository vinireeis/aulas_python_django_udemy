lista_a = [10, 2, 3, 40, 5, 6]
lista_b = [1, 2, 3, 4]
lista_soma = []

if len(lista_a) < len(lista_b):
    for x in range(len(lista_a)):
        lista_soma.append(lista_a[x] + lista_b[x])
else:
    for x in range(len(lista_b)):
        lista_soma.append(lista_a[x] + lista_b[x])
print(lista_soma)

lista_total = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_total)
