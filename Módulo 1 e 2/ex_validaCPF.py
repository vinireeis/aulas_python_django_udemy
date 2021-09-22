cpf = input('Informe o seu cpf: ')
# cpf = 16899535009
new_cpf = cpf[0:9]
reverso = 10
tot = 0


for index in range(19):
    if index > 8:
        index -= 9

    tot += int(new_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (tot % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)
sequencia = new_cpf == str(new_cpf[0]) * len(cpf)
if cpf == new_cpf and not sequencia:
    print('cpf válido')
else:
    print('inválido')


'''
tot_cpf = 0
cont = 0
for x in range(10, 1, -1):
    tot_cpf += new_cpf[cont] * x
    cont += 1
    print(new_cpf[cont], 'x', x, f'total {tot_cpf,}')
print(tot_cpf)'''
