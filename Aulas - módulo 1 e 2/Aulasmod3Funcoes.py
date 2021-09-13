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
print('-=' * 20)

print('funcoes lambda')
''' funcoes lambda (anonimas)'''
print('-' * 40)


def mult(x, y):
    return x * y


multiplica = mult(3, 6)
print(f'{multiplica} essa é funcao padrao, nomeada')
print('-' * 40)
# se trata da mesma função acima, porém no formato lambda (anonima)
# pois não tem nome
def a(x, y): return x * y


b = lambda x, y: x * y


print(f'{b(5, 10)} essa é lambda')
print('-' * 40)

n_lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 9]
]


def ordene(item):
    return item[1]


n_lista.sort(key=ordene)
print(n_lista)

n_lista.sort(key=ordene, reverse=True)
print(n_lista)

# com lambda

n_lista.sort(key=lambda item: item[1])
print(n_lista)

# outra forma

print(sorted(lista, key=lambda i: i[1]))
