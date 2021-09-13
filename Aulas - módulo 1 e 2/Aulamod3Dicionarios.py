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