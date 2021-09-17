from itertools import groupby

alunos = [
    {'nome': 'Vinicius',
     'nota': 'A'},
    {'nome': 'Letícia',
     'nota': 'B'},
    {'nome': 'Rafael',
     'nota': 'C'},
    {'nome': 'Douglas',
     'nota': 'A'},
    {'nome': 'Larissa',
     'nota': 'A'},
    {'nome': 'Débora',
     'nota': 'B'},
    {'nome': 'Cintia',
     'nota': 'A'},
    {'nome': 'Thiago',
     'nota': 'D'},
    {'nome': 'Eder',
     'nota': 'A'},
    {'nome': 'Carol',
     'nota': 'C'}
]

for nota in alunos:
    print(nota)

print('\n')
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)  # agrupou os alunos pela nota
'''
for agrupado in alunos_agrupados:  # para visualizar
    print(agrupado)

# para melhor visualizar
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()
'''
# saber quantidade de alunos por grupo
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    print(f'{len(list(valores_agrupados))}')