nome = str(input('Informe o seu primeiro nome: ').lower())
if nome.isalpha():
    if len(nome) < 5:
        print('Seu nome é curto')
    elif len(nome) in range(5, 6+1):
        print('Seu nome é de tamanho médio')
    else:
        print('Seu nome é muito grande')
else:
    print('Informe um nome somente com string')
