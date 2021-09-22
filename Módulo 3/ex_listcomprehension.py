string = '012345678901234567890123456789012345678901234567890123456789'

l1 = [letra for letra in string]
print(l1)
n = 10  # nao precisaria usar N pois o valor é fixo.
tupla = [(i, i + 10) for i in range(0, len(string), 10)]
#  transformando em tupla para melhor compreensao
print(tupla)
raw = [f'string[{i}:{i + 10}]' for i in range(0, len(string), 10)]
#  transformando em tupla para melhor compreensao
print(raw)
l2 = [string[i: i + n] for i in range(0, len(string), n)]  # fatiando a string
print(l2)
retorno = '.'.join(l2)
print(retorno)
