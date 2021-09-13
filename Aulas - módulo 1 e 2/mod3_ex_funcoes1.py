def recebe(funcao):
    return funcao()


def arg():
    return 'Vinicius teste'


x = recebe(arg)
print(x)

# criar fun1 que recebe fun2 como parametro e retorne o valor
# da fun2. faça a fun1 executar duas funcoes que recebam um
# numero diferente de argumentos


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


exec = mestre(fala_oi, 'Vini')
print(exec)

exec1 = mestre(saudacao, 'Vini', saudacao='Bom dia')
print(exec1)
