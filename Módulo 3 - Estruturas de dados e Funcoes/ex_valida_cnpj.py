"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import re


def format_doc(doc):
    return list(re.sub(r'[^0-9]', '', doc))


def calculo_cnpj(doc):
    #  primeiro calculo
    del doc[-2:]
    calc_1 = ['5', '4', '3', '2', '9', '8', '7', '6', '5', '4', '3', '2']
    calc_cnpj = 11 - ((sum([int(x) * int(y)
                      for x, y in zip(calc_1, doc)])) % 11)
    calc_cnpj = calc_cnpj if calc_cnpj < 10 else 0
    doc.append(str(calc_cnpj))
    #  segundo calculo
    calc_2 = ['6', '5', '4', '3', '2', '9', '8', '7', '6', '5', '4', '3', '2']
    calc_cnpj = 11 - ((sum([int(x) * int(y)
                      for x, y in zip(calc_2, doc)])) % 11)
    calc_cnpj = calc_cnpj if calc_cnpj < 10 else 0
    doc.append(str(calc_cnpj))
    return doc


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def valida_cnpj(cnpj_original):
    sequencia = eh_sequencia(cnpj_original)
    if sequencia:
        return print('CNPJ informado inválido, pois é uma sequencia')
    novo_cnpj = format_doc(cnpj_original)
    novo_cnpj = calculo_cnpj(novo_cnpj)
    cnpj_original = format_doc(cnpj_original)
    if cnpj_original == novo_cnpj:
        return print('CNPJ VÁLIDO')
    return print('CNPJ INVÁLIDO')


if __name__ == '__main__':
    cnpj_original = '11111111111111'
    valida_cnpj(cnpj_original)
