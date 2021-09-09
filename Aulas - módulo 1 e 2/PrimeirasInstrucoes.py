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
# validar se é um 'digito', inteiro e positivo > isdigit()

n1 = input('Digite um número: ')
n2 = input('Digite um número: ')

if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    print('Após a validação da condição, os valores foram convertidos'
          ' para inteiros e somados, tendo como resultado', n1 + n2)
else:
    print('Não pude converter os valores informados')
print('-' * 40)
print('Formatando valores com modificadores - aula 5')
# s - string, d - inteiro, f - float
# .2f  > quantidade de caracteres decimais depois da virgula/ponto.
# (CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO) exemplos abaixo
# maior > - coloca a esquerda
# menor < - coloca a direita
# ^ - Centro

n1 = 1
n2 = 1150
n3 = 249.3950128
# > significa que colocará os zeros até completar dez digitos.
print(f'{n1:0>10}')
print('-' * 40)
print(f'{n2:0^8}')  # centro
print('-' * 40)
print(f'{n3:.2f}')  # float
print('-' * 40)
print(f'{n2:0>10.2f}')  # colocando valores e decimais.
print('-' * 40)
nome = 'Vinicius Reis'
print(f'{nome:#^50}')
# n1.ljust(20, #) mesma coisa que :{n1:#<20}
print('-' * 40)
print('Aula 6 - manipulando strings')
# +[0123456789]
# -[987654321]
n = 'Python <3'
print(n[-5])  # posição -5 da string
# fatiamento n[0:6] vai imprimir do 0 até a posição 5
print(n[0:6])
# fatiamento pulando caracteres
# primeiro valor é o inicio, segundo é o fim, terceiro é de quantos em quantos irá pular.
print(n[0:8:3])
print('-' * 40)

frase = 'O rato roeu a roupa do rei de roma'
tm_frase = len(frase)
contador = 0
nova_frase = ''

while contador < tm_frase:
    print(frase[contador], contador)
    nova_frase += frase[contador]
    contador += 1
print(nova_frase)

# for x in range(20, 10, -1)  20 = número que começa, 10 - 1 número que termina , -1 vai subtrair -1 em cada passagem do loop
for x in range(20, 10-1, -1):
    print(x)
print('-' * 40)
# trocando valores

x = 10
y = 'Vinicius'
z = 15.87
x, y, z = z, x, y
print(x, y, z)
print('-' * 40)

# podemos usar o OR ou AND dentro do print
nome = input('Qual seu nome?')
print(nome or 'Você não digitou nada')
print('-' * 40)
# usando if/else dentro da variável
idade = input('Informe a sua idade: ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números')
de_maior = (int(idade) >= 18)
msg = 'Pode acessar' if de_maior else 'Não pode acessar'
print(msg)
