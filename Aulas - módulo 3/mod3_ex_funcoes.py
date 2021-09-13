def saudacao(a, b):
    return (a, b)


print(saudacao('Olá', 'Vinicius'))


def soma(a, b, c):
    return (a + b + c)


print(soma(2, 10, 15))


def aumento(x, y):
    return (x + (x * (y / 100)))


print(aumento(1500, 15))


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    return n


print(fizzbuzz(15))
print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(7))
