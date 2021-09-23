"""
public, protected, private
_ "protected"
__ "private"
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_dados(self, id, nome):
        if 'clientes' not in self.__dados:
            # se não existir, vai cadastrar
            self.__dados['clientes'] = {id, nome}
        else:
            # se já existir, vai atualizar
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    @property
    def get_dados(self):
        return self.__dados


bd = BaseDeDados()
bd.inserir_dados(1, 'Vinicius')
bd.inserir_dados(2, 'Larissa')
bd.lista_clientes()
bd.__dados = 'Outra coisa'
# isso quebraria os métodos caso fosse público ou só com um..
#  "underline" > self.dados ou self._dados
# mas como definimos da forma mais "protegida" com __dados ele irá criar..
#  um novo atributo
# e o atributo original será renomeado para _BaseDeDados__dados
# O padrão é _NomeDaClasse__nome_atributo
print(bd.__dados)
print(bd._BaseDeDados__dados)
# bd.lista_clientes() agora já não funciona mais por ter alterado a estrutura..
#  da classe e o método não estar preparado para isso
