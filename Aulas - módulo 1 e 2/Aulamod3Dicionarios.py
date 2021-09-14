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
for x in d1.keys():  # acessando apenas as chaves
    print(x)

for y in d1.values():  # acessando apenas os valores
    print(y)

for z in d1.items():
    print(z)

for k in d1.items():  # acessando chave e valor
    print(k[0], k[1])

for u, t in dic.items():  # acessando chave e valor
    print(u, t)

# desempacotando

clientes = {
    'cliente1': {
        'nome': 'Vinicius',
        'sobrenome': 'Reis'
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Larissa',
        'sobrenome': 'Costa'
    }
}
print('-=' * 20)

for clientes_k, clientes_v in clientes.items():
    print(f' Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# fazendo uma cópia de um dicionário.
v = d1.copy()
v['chave1'] = 'Vinicius copy'
print(d1)
print(v)

# convertendo para um dicionário dict()

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
print('-=' * 20)
d10 = dict(lista)
print(d10)

d10.pop('c3')  # elimina a chave mencionada
print(d10)
d10.popitem()  # elimina o último elemento
print(d10)

d10.update((d1))
print(d10)

