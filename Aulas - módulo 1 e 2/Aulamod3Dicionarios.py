dic = {'chave1': 'valor da chave'}
dic['new_key'] = 'new value of key'

print(dic['chave1'])

# outra forma de criar
d1 = dict(chave1='Valor da chave1', chave2='Valor da chave2')
print(d1)
# exemplo

d2 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla'
}

d2['str'] = 'Agora ela existe'
# forma de verificar se existe uma chave
if d2.get('str') is not None:
    print(d2.get('str'))

# apagando algo
del d2['str']
print(d2)
d2['str'] = 'valor'

print('str' in d1)  # false

print('valor' in d2.values())  # true

# saber o tamanho utilizar o len
# print(len(d1))

# para ver values, keys e items(pares)
for x in d1.keys():
    print(x)

for y in d1.values():
    print(y)

for z in d1.items():
    print(z)

for k in d1.items():
    print(k[0], k[1])

for k, v in dic.items():
    print(k, v)

# desempacotando
