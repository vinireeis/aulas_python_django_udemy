import json

# sobre abertura, leitura e gravação de arquivos.
file = open('arqaula.txt', 'w+')  # w+ limpa o arquivo e permite escrita
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')
file.seek(0, 0)  # para voltar ao topo do arquivo (cursor para o começo)
print('Lendo linhas: ')
print(file.read())  # para ler o arquivo, porém ele vai ler da linha 7 pra frente
print('---------------------------')
file.seek(0, 0)
print(file.readline(), end='')  # começa a ler de onde ele parou
print(file.readline(), end='')  # quebra de linha do print por isso o end
print(file.readline(), end='')
file.seek(0, 0)
print(file.readlines())  # imprime como lista
print()
print('USANDO TRY\n')
file.close()
# forma que é geralmente utilizada
try:
    file = open('arqaula1.txt', 'w+')
    file.write('Linha1\n')
    file.seek(0)
    print(file.read())
finally:
    file.close()


# usando outra forma
# com este gerenciador de contexto ele mesmo já fecha o arquivo
# é a melhor maneira de se trabalhar com arquivos em python.
with open('arqaula.txt', 'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())

# r+ funciona para ler o arquivo
# a+ funciona para ler e append mode, sem apagar o arquivo (como w+ faz)

# import os >> os.remove('nomedoarquivo.txt') deleta o arquivo criado

# exemplo de converter para json
d1 = {
    'Pessoa1':{
        'nome': 'Vinicius',
        'idade': 27,
    },
    'Pessoa2':{
        'nome': 'Lucas',
        'idade': 35,
    }
}
# fazendo um dicionario virar um json
d1_json = json.dumps(d1, indent=True)
print(d1_json)

'''
fazendo um json, voltar a ser um dicionário.
import json

with open('teste.json', 'r') as file:
    d1_json = json.loads(d1_json)
    print(d1_json

assim voltará a ter as chaves acessíveis, pois foi convertido em dicionário
'''