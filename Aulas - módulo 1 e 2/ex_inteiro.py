while True:
    n = input('Informe um número inteiro: ')

    if n.isnumeric() is True:
        if int(n) % 2 == 0:
            print(f'O valor {n} é par')
        else:
            print(f'O valor {n} é ímpar')
            break
    else:
        print('Erro! Informe um número inteiro')
