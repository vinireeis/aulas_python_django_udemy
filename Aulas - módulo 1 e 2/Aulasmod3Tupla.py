t1 = (1, 2, 3, 'a', 'Vinicius')
# t1 = (1, 2, 3, 'a', 'Vinicius') * 20   >> forma de multiplicar uma tupla
print(t1[4])

for x in t1:
    print(x)

print(t1[2:])  # fatiamento
print(type(t1))

t2 = 6, 7, 8, 9
t3 = t1 + t2

n1, n2, n3, *_, ultimo = t3  # desempacotamento da tupla

print(f'{n1}, {n2}')
print(*_)
print(ultimo)

t4 = 1, 2, 3
t4 = list(t4)
t4[1] = 3000
t4 = tuple(t4)
print(t4)
