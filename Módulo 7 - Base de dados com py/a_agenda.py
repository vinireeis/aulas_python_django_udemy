import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        update = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(update, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id):
        delete = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(delete, (id, ))
        self.conexao.commit

    def listar(self):
        select = 'SELECT * FROM agenda'
        self.cursor.execute(select)

    def buscar(self, elemento):
        select = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(select, (f'%{elemento}%', ))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conexao.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Vinicius', '952945737')
    # agenda.inserir('Guilherme', '652945737')
    # agenda.inserir('Larissa', '956707888')
    # agenda.inserir('Maria', '951238587')
    # agenda.listar()
    # agenda.editar('Francisco1', '969878864', 4)
    # agenda.listar()
    # agenda.excluir(4)
    # agenda.listar()
    agenda.inserir('Marcos Vinicius', '652634737')
    agenda.inserir('Vinicius Souza', '956582888')
    agenda.inserir('Paulo Vinicius', '951238587')
    agenda.listar()
    agenda.buscar('Vinicius')
    agenda.listar()
    agenda.fechar()
