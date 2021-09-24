from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.nomeclasse = self.__class__.__name__

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer pois está falando')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        elif self.falando:
            print({f'{self.nome} já está falando'})

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 99999)
        return rand


"""utiliando herança"""


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(self, nome, idade)
        self.sobrenome = sobrenome  # sobrescrevendo com um atributo específico


"""
    def falar(self, assunto):
        print('Falando outra coisa qualquer')  # sobrescrevendo o método
        return super().falar(assunto)  # chamando o falar da superclasse Pessoa



Cliente é uma herança simples, pois herda apenas de Pessoa.
ClienteVIP é uma herança múltipla, pois Cliente VIP herda de Cliente que herda
de Pessoa, ou seja, ClienteVip terá todas as definições da classe
Pessoa e Cliente
"""
