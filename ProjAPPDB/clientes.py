from banco import Banco
import tkinter.messagebox as msgbox

class Clientes(object):

    def __init__(self, idclientes=0, cliente="", cidade="",
                 endereco="", telefone="", email=""):
        self.info = {}
        self.idclientes = idclientes
        self.cliente = cliente
        self.cidade = cidade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def insertCli(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_clientes(cliente, cidade, endereco, telefone, email) values (?, ?, ?, ?, ?)",
                      (self.cliente, self.cidade, self.endereco, self.telefone, self.email))
            banco.conexao.commit()
            c.close()
            msgbox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            msgbox.showerror("Erro", f"Erro na inserção do cliente: {e}")

    def updateCli(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_clientes set cliente = ?, cidade = ?, endereco = ?, telefone = ?, email = ? where idclientes = ?",
                      (self.cliente, self.cidade, self.endereco, self.telefone, self.email, self.idclientes))
            banco.conexao.commit()
            c.close()
            msgbox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        except Exception as e:
            msgbox.showerror("Erro", f"Erro na atualização do cliente: {e}")

    def deleteCli(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_clientes where idclientes = ?", (self.idclientes,))
            banco.conexao.commit()
            c.close()
            msgbox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            msgbox.showerror("Erro", f"Erro na exclusão do cliente: {e}")

    def selectCli(self, idclientes):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_clientes where idclientes = ?", (idclientes,))
            linha = c.fetchone()
            if linha:
                # Preencher os atributos da classe com os dados retornados
                self.idclientes, self.cliente, self.cidade, self.endereco, self.telefone, self.email = linha
                c.close()
                msgbox.showinfo("Sucesso", "Cliente encontrado com sucesso!")
                return True  # Dados encontrados
            else:
                msgbox.showwarning("Aviso", "Cliente não encontrado.")
                return False  # Cliente não encontrado
        except Exception as e:
            msgbox.showerror("Erro", f"Erro na busca do cliente: {e}")
            return False  # Erro ao buscar cliente

    def selectAllCli(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            msgbox.showerror("Erro", f"Ocorreu um erro na recuperação dos clientes: {e}")
