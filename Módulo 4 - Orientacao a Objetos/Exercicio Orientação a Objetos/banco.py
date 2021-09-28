from abc import ABC, abstractmethod


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.agencias = []
        self.contas = []
        self.clientes = []

    def incluir_conta(self, conta):
        self.contas.append(conta)

    def incluir_agencia(self, agencia):
        if type(agencia) == list:
            for x in agencia:
                self.agencias.append(x)
                return
        self.agencias.append(agencia)

    def incluir_cliente(self, cliente):
        self.clientes.append(cliente)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        print(self.contas)
        for x in cliente.contas:
            if x not in self.contas:
                return False
            if x.agencia not in self.agencias:
                return False
        return True


class Conta(ABC):
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.get_saldo()

    def get_saldo(self):
        return print(f'Conta: {self.numero}\nAgência: {self.agencia}\n'
                     f'Seu saldo é: R${self.saldo: 0.2f}')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero):
        super().__init__(agencia, numero)
        self.saldo = 0
        self.limite = 500

    def sacar(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor
            print('Saque com sucesso')
        else:
            return 'Saldo insuficiente'


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero):
        super().__init__(agencia, numero)
        self.saldo = 0

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            return print('Saldo insuficiente')
