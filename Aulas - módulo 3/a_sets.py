# formas de criar
s1 = set()
s2 = {1, 2, 3, 4}

# adicionar valor

s1.add(6)
s1.add(7)
s1.add(8)
s1.add((1, 2, 3, 'Vinicius'))
print(s1)
print(s2)

s1.discard(6)  # removendo um elemento
print(s1)
s3 = set()
# existe o comando clear também.
# adciona o valor, porém itera sobre ele.
s3.update('Python')
print(s3)

# set nao aceita duplicados
s4 = set()
s4.update([1, 2, 3, 4, 5], {5, 6, 1})
print(s4)
# removendo duplicados
l1 = [1, 2, 3, 3, 4, 4, 1, 1, 5, 6, 6, 8]
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)
print('-' * 40)

# concatenando sets
# union |
s5 = {1, 2, 3, 4, 5, 7}
s6 = {1, 2, 3, 4, 5, 6}
s7 = s5 | s6
print(s7)
# intersection &
s8 = s5 & s6
print(s8)
# difference
s9 = s5 - s6 # diferenca do primeiro set para o segundo ( da esquerda para a direita)
print(s9)
# symmetric_difference
# valores únicos nos dois sets
s10 = s5 ^ s6
print(s10)
# forma de comparar listas usando set
l1 = ['Vinicius', 'Larissa', 'Cintia']
l2 = ['Vinicius', 'Vinicius', 'Vinicius', 'Vinicius', 'Cintia', 'Cintia', 'Larissa', 'Larissa']
print(l1 == l2)  # false
l1 = list(set(l1))
l2 = list(set(l2))  # já convertendo em lista novamente
print(l1 == l2)  # true
print(l1, l2)
print('-' * 40)

# agora se não quiser alterar os valores da lista, podemos usar somente com condicao
l3 = ['Vinicius', 'Larissa', 'Cintia']
l4 = ['Vinicius', 'Vinicius', 'Vinicius', 'Vinicius', 'Cintia', 'Cintia', 'Larissa', 'Larissa']
if set(l3) == set(l4):  # que vai ser True
    print('L3 é igual a L4')
# porem se printar as listas verá que o valor não foi modificado
print(l3)
print(l4)