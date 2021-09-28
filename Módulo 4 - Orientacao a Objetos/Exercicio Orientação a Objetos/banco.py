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
            return self.agencias
        return self.agencias.append(agencia)

    def incluir_cliente(self, cliente):
        self.clientes.append(cliente)


class Conta(ABC):
    def __init__(self, agencia, numero):
        self.agencia = agencia
        self.numero = numero
        self.__saldo = 0

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    @property
    def get_saldo(self):
        return print(f'Seu saldo é: R${self.__saldo:0.2f}, conta: {self.numero}'
                     f' e agência {self.agencia}')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero):
        super().__init__(agencia, numero)
        self.__saldo = 0
        self.limite = 500

    def sacar(self, valor):
        if valor <= self.limite:
            self.limite -= valor
            self.__saldo -= valor
            return self.__saldo
        else:
            return 'Saldo insuficiente'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return self.__saldo
        return print('Valor não permitido')

    def get_saldo(self):
        return print(f'Seu saldo é: R${self.__saldo:0.2f}, conta: {self.numero}'
                     f' e agência {self.agencia}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero):
        super().__init__(agencia, numero)
        self.__saldo = 0

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return self.__saldo
        else:
            return 'Saldo insuficiente'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return self.__saldo
        return print('Valor não permitido')

    def get_saldo(self):
        return print(f'Seu saldo é: R${self.__saldo:0.2f}, conta: {self.numero}'
                     f' e agência {self.agencia}')
