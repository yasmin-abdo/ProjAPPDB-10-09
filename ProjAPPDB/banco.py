import sqlite3   # banco padrão do banco de dados do python
# gerencia o banco = banco.py


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUsuarios()
        self.createTableClientes()
        self.createTableCidades()

    def createTableUsuarios(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario integer primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")
        self.conexao.commit()
        c.close()

    def createTableCidades(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_cidades(
        idcidades integer primary key autoincrement,
        nome text,
        uf text)""")
        self.conexao.commit()
        c.close()

    def createTableClientes(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_clientes(
        idclientes integer primary key autoincrement,
        cliente text,
        cidade text,
        endereco text,
        telefone text,
        email text)""")
        self.conexao.commit()
        c.close()





