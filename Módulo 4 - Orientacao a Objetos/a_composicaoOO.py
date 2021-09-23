from carrinho import Produto, CarrinhoDeCompras
from carrinho import Endereco, Cliente

produto1 = Produto('Camiseta', 100)
produto2 = Produto('Iphone', 5300)
produto3 = Produto('Caneca', 30)
carrinho = CarrinhoDeCompras()

carrinho.inserir_produtos(produto1)
carrinho.inserir_produtos(produto2)
carrinho.inserir_produtos(produto3)
carrinho.inserir_produtos(produto2)
carrinho.lista_produtos()
print(carrinho.soma_total())
print()

""" mostrando composição """

cliente1 = Cliente('Vinicius', 27)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Larissa', 22)
cliente2.insere_endereco('Recife', 'PE')
print(cliente2.nome)
cliente2.lista_endereco()
print()
del cliente2
# Repare que ao apagar o cliente, a instância da classe Endereco também é..
# excluida, pois é uma composição da classe Cliente.
print('###################################')

# aqui tudo é apagado por padrão do python,
