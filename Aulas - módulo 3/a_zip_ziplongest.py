from itertools import zip_longest, count

cidades = ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Monte Belo']
estados = ['SP', 'RJ', 'BA']
indice = count()
cidades_estados = zip(estados, cidades)

cid_est_zip = zip(indice, estados, cidades)  # n da pra usar filter
for valor in cid_est_zip:
    print(valor)  # pode travar o pc zip_longest n tem fim
'''
cid_est = zip_longest(indice, estados, cidades, fillvalue='Estado')
for valor in cid_est:
    print(valor)  # pode travar o pc zip_longest n tem fim

for valor in cidades_estados:  # dessa forma verá tuplas
    print(valor)

for valor in cidades_estados:
    print(valor[0], valor[1])  # desempacota

for valor in cidades_estados:  # dessa forma verá tuplas
    print(valor)  # nao vai mostrar nada porque esgotou o gerador anterior(for)


cid_est = zip_longest(indice, estados, cidades, fillvalue='Estado')
# para preencher os None com um valor padrão
print(list(cid_est))  # vai travar o pc pois o count() não tem fim'''
