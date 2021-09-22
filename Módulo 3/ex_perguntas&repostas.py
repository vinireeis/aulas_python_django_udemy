perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '3'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
            'pergunta': 'Quanto é 3*2?',
            'respostas': {'a': '10', 'b': '14', 'c': '6'},
            'resposta_certa': 'c'
    }
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv["respostas"].items():
        print(f'{rk}: {rv}')

    resp = input('Qual a resposta correta? ')
    if resp == pv['resposta_certa']:
        print('Parabéns, correto!')
    else:
        print('Errouuu :/ ')
