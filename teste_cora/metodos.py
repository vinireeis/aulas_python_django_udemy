def instance_answer(lista):
    minimo = min(lista)
    maximo = max(lista)
    quantidade = len(lista)
    total = 0
    for n in lista:
        total += n
    media = total/quantidade

    return minimo, maximo, quantidade, media


def media(lista):
    total = 0
    n_elementos = len(lista)
    for n in lista:
        total += n
    return total / n_elementos


def quantidade(lista):
    cont = 0
    for n in lista:
        cont += 1
    return cont


def minimo(lista):
    copia = lista[0]
    for n in lista:
        if copia > n:
            copia = n
    return copia


def maximo(lista):
    copia = lista[0]
    for n in lista:
        if copia < n:
            copia = n
    return copia
