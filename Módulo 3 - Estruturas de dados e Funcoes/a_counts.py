from types import GeneratorType
from itertools import count

variavel = zip('alo', 'alo')  # isso é uma string iteravel
# print(list(variavel)) # variavel é uma string iterável
print(next(variavel))  # zip é um iterador
print(next(variavel))  # zip é um iterador
print(next(variavel))  # zip é um iterador

print(isinstance(variavel, GeneratorType))  # false pois não é gerador

# exemplo de transformar em gerador
var = ((x, y) for x, y in zip('alo', 'alo'))
print(isinstance(var, GeneratorType))  # agora sim é um gerador

'''
count - Itertools
'''

contador = count(start=0, step=2)  # start qnto começa, step qnto pula
cont = count(start=5, step=0.1)  # é possivel pular em float
# é um iterador, cuidado ao usar para n cair em um loop infinito
print(next(contador))  # 0
print(next(contador))  # 2
print(next(contador))  # 2
print('\n')
for valor in cont:
    print(round(valor, 2))
    if valor >= 10:
        break

cont1 = count(start=9, step=-1)  # seria um loop infinito negativo
# caso não coloque uma condição de parada
