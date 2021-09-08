n = input('Informe um número inteiro: ')

if True:
    if n.isnumeric():
        if int(n) % 2 == 0:
            print(f'O valor {n} é par')
        else:
            print(f'O valor {n} é ímpar')
    else:
        print('Erro! Informe um valor correto.')