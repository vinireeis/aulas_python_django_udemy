from pessoa import Cliente, Aluno, ClienteVip

c1 = Cliente('Luiz', 45)
c1.falar('Motos')
c1.comprar()

a1 = Aluno('Maria', 54)
a1.falar('gastronomia')
a1.estudar()

"""
Podemos ver que apresenta o nome da classe referente a instância do objeto
A def FALAR está na classe mãe e foi herdado pelas classes filhas.
Enquanto comprar e estudar são específicos das classes filhas, aluno e cliente
"""
print('\n')

c2 = ClienteVip('Antonio', 17, 'Pereira')
