from collections import deque

fila = deque()
fila.append('Vinicius')
fila.append('Larissa')
fila.append('José')
fila.append('Maria')
print(fila)

fila.popleft()
print(fila)


fila1 = deque(maxlen=5)  # remove o elemento mais antigo para entrar um novo
# assim que atingir o maxlen
fila1.extend([1, 2, 3, 4, 5])
print(fila1)
fila1.append(6)
print(fila1)

# fila.insert(2, 'Vinicius Reis') insere Vinicius Reis na posição 2.
# extend recebe iteravel [1, 2, 3] e append recebe apenas um elemento (4)
# fila.index (2) vai retornar o valor do index do elemento 2 se estiver na fila
# fila.reverse, inverte a ordem da fila
# fila.rotate(2) pega os dois ultimos elementos e colocaria no começo da fila
