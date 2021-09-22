from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Vinicius', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('Combinations - combinações únicas onde a ordem não imrpota')
for grupo in combinations(pessoas, 2):
    print(grupo)
print('\n')
print('Permutations - combinações onde a ordem importa andre-luiz , luiz-andre')
for grupo in permutations(pessoas, 2):
    print(grupo)
print('\n')
print('Product - todas combinações possíveis')
for grupo in product(pessoas, repeat=2):
    print(grupo)