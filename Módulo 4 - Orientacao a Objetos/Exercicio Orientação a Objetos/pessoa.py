from banco import Banco, Conta, ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def get_nome(self):
        return self.nome

    @property
    def get_idade(self):
        return self.idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.contas = []

    def incluir_conta(self, conta):
        self.contas.append(conta)
        return self.contas

    def get_contas(self, banco):
        for x in self.contas:
            if x.agencia in banco.agencias:
                return print(
                    f'Seu banco: {banco.nome}, agencia: {x.agencia} conta: {x.numero}')
        return print('Você não tem contas nesse banco')
