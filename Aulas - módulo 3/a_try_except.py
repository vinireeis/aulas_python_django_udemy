# https://docs.python.org/3/library/exceptions.html
try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
# else é executado sempre que não há erro.
finally:
    print('Finally é sempre executado independente se há erro ou não')

print()
print('-' * 50)
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise
try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print('Relançando', error)

print()
print('-' * 50)

def divide1(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2

print(divide1(2,0))


# ultimo exemplo

def converte_numero(valor):
    try:
        valor = int(valor)
    except ValueError:
        try:
            valor = float(valor)
        except ValueError:
            pass
# primeiro validamos se conseguimos converter para inteiro
# caso não seja possível, tentamos converter para float
# caso não seja int nem float, é um erro pois não é um número.

while True:
    numero = converte_numero(input('Digite um numero: '))

    if numero is not None:
        print(numero * 5)
    else:
        print('Erro: isso não é um número')
