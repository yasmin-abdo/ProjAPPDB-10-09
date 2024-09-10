from banco import Banco
from tkinter import messagebox

class Cidades(object):

    def __init__(self, idcidades=0, nome="", uf=""):
        self.info = {}
        self.idcidades = idcidades
        self.nome = nome
        self.uf = uf

    def insertCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into tbl_cidades (nome, uf) values (?, ?)", (self.nome, self.uf))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade cadastrada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na inserção da cidade: {e}")

    def updateCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_cidades set nome = ?, uf = ? where idcidades = ?", (self.nome, self.uf, self.idcidades))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na atualização da cidade: {e}")

    def deleteCid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            # Verifica se há clientes associados à cidade
            c.execute("select count(*) from tbl_clientes where cidade = ?", (self.nome,))
            clientes_count = c.fetchone()[0]

            if clientes_count > 0:
                messagebox.showerror("Erro",
                                     "Não é possível excluir a cidade porque está associada a um ou mais clientes.")
                return

            # Exclui a cidade se não houver clientes associados
            c.execute("delete from tbl_cidades where idcidades = ?", (self.idcidades,))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade excluída com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro na exclusão da cidade: {e}")

    def selectCid(self, idcidades):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from tbl_cidades where idcidades = ?", (idcidades,))
            linha = c.fetchone()
            if linha:
                self.idcidades, self.nome, self.uf = linha
                c.close()
                messagebox.showinfo("Sucesso", "Busca feita com sucesso!")
            else:
                messagebox.showwarning("Não Encontrado", "Cidade não encontrada.")
                self.limparCampos()  # Limpar campos se a cidade não for encontrada
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na busca da cidade: {e}")

    def selectAllCids(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na recuperação das cidades: {e}")
            return []


