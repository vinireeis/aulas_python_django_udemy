carrinho = [
    ('Produto1', 30),
    ('Produto2', 20),
    ('Produto3', 50),
    ('Produto4', 99),
    ('Produto5', '30'),
    ('Produto6', 50.50),
    ('Produto7', 150),
    ('Produto8', 10),

]

l1 = sum([float(x[1]) for x in carrinho])
print(l1)
