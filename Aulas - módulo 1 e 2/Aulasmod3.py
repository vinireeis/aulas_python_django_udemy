# aula sobre args e kwargs
# *args é utilizado quando não sabemos a quantidade de parametros a ser passado.
def func(*args):
    # args é tupla, e fizemos isso para poder converter em lista e posteriormente alterar uma posição
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)  # insere esses valores na func


def func1(*args):
    for v in args:
        print(v)  # printando os valores passados para a func


func1(0, 10, 15, 9, 8, 7)


def func2(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func2(*lista, *lista2)
# para juntar tudo no print, precisamos desempacotar a lista


def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    # podemos referenciar da mesma forma que o dicionário.
    print(kwargs['nome'], kwargs['sobrenome'])
    # outra forma de verificar se existe uma chave no kwargs é utilizar a funcao get
    nome = kwargs.get('nome')
    print(nome)
    # porem se for feito com algo que não existe, retornará NONE, diferente de um erro que retornaria na primeira forma
    idade = kwargs.get('idade')
    print(idade)


print('-' * 50)
# para passar valores kwargs, é utilizado os keywords como um dicionário
# chave e valor
lista3 = [1, 2, 3, 4, 5]
lista4 = [10, 20, 30, 40, 50]
func3(*lista3, *lista4, nome='Vinicius', sobrenome='Reis')
print('-' * 50)
