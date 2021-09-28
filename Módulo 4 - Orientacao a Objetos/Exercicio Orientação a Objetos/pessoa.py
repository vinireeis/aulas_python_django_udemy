class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_idade(self):
        return self._idade


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
                    f'Seu banco: {banco.nome}, agencia: {x.agencia} conta: '
                    f'{x.numero}')
        return print('Você não tem contas nesse banco')
