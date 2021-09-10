# aula sobre args e kwargs
# *args é utilizado quando não sabemos a quantidade de parametros >>
# a ser passado.
def func(*args):
    # args é tupla, e fizemos isso para poder converter em lista e >>
    # posteriormente alterar uma posição
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
# outra forma de verificar se existe uma chave no kwargs é utilizar >>
# a funcao get
    nome = kwargs.get('nome')
    print(nome)
# porem se for feito com algo que não existe, retornará NONE, diferente de >>
# um erro que retornaria na primeira forma
    idade = kwargs.get('idade')
    print(idade)
# outra maneira de prever este erro é usando um >>
#  if idade is not None: print(idade)


print('-' * 50)
# para passar valores kwargs, é utilizado os keywords como um dicionário
# chave e valor
lista3 = [1, 2, 3, 4, 5]
lista4 = [10, 20, 30, 40, 50]
func3(*lista3, *lista4, nome='Vinicius', sobrenome='Reis')
print('-' * 50)

# variáveis globais e alteração por dentro de funções
variavel = 'valor'


def var():
    print(variavel)


def var1():
    variavel = 'Novo valor'
    print(variavel)


var()  # printa a variável global.
var1()  # printa a variável que está dentro da var1
print(variavel)  # printa a variavel global

# formas de alterar o valor da variável globa/local(dentro da funcao)


def var2():
    global variavel
    variavel = 'Terceiro valor'
    print(variavel)


var2()
# veja que alteramos o valor da variavel global, porém não é uma prática >>
#  recomendada, pode causar problemas alterar variaveis globais pela função.
print(variavel)

# uma forma melhor de lidar com ela.


def var3(arg=None):
    arg = arg.replace('T', 'Q')
    return arg


nova_var = var3(arg=variavel)  # passando o "Terceiro Valor" para a func var3
print(nova_var)
'''assim trabalhamos com o valor da "variavel", mas não foi
alterada globalmente, evitando problemas'''

''' nao é possível mesclar variavel global e local
ao ter uma variavel global e tentar muda-la de valor retornará um erro
pois ela já foi definida anteriormente'''

# passar valor de uma para outra, alternativa.


def fun():
    n_var = 'Vinicius Reis'
    return n_var


def fun1(arg):
    print(arg)


var = fun()
fun1(var)
