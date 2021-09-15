lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

if lista.reverse() == list(set(lista)):
    print('são iguais')
else:
    print('são diferentes')

print('-' * 35)

