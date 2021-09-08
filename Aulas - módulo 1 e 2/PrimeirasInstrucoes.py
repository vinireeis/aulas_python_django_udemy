print('Hello, World!')
print('-' * 40)
# separador > print('Vinicius', 'Reis', sep='/')
# remover quebra de linha > print('Vinicius', end='')
print('250', '450', '785', sep='.', end='-')
print('18')
print('-' * 40)
# utilizar aspas > print('Esse
print(10 // 3)  # divisão inteira //
print('-' * 40)
# operadores lógicos aula 4
# and, or, not, in, not in.
a = ''
if not a:
    print('Por favor preencha o valor de A.')
print('-' * 40)
#
if False:
    print('Um')
elif False:
    print('Dois')
elif False:
    print('Três')
elif True:
    print('Quatro')
elif False:
    print('Cinco')
else:
    print('Seis')

# validar se é um número, inteiro e positivo > isnumeric()
#validar se é um 'digito', inteiro e positivo > isdigit()

n1 = input('Digite um número: ')
n2 = input('Digite um número: ')

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print('Após a validação da condição, os valores foram convertidos'
          ' para inteiros e somados, tendo como resultado', n1 + n2)
else:
    print('Não pude converter os valores informados')