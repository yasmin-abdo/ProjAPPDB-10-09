from banco import Banco
from tkinter import messagebox


class Usuarios(object):

    def __init__(self, idusuario=0, nome="", telefone="",
                 email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_usuarios (nome, telefone, email, usuario, senha) values (?, ?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na inserção do usuário: {e}")

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_usuarios set nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? where idusuario = ?",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na atualização do usuário: {e}")

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_usuarios where idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na exclusão do usuário: {e}")

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_usuarios where idusuario = ?", (idusuario,))
            linha = c.fetchone()
            if linha:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
                messagebox.showinfo("Sucesso", "Busca feita com sucesso!")
            else:
                messagebox.showwarning("Não Encontrado", "Usuário não encontrado.")
            c.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca do usuário: {e}")

    def selectAllUsers(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na recuperação dos usuários: {e}")
            return []



