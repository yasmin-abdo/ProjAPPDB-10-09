from tkinter import *
from tkinter import ttk
from cidades import Cidades
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox

class Cidade:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    # TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Cadastro de Cidades\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()

    # ID CIDADE
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="Buscar ID: \n", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 18
        self.id["font"] = self.fontepadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, font=self.fontebotao)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.buscarCidades

    # NOME CIDADE
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome Cidade: \n", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 24
        self.nome["font"] = self.fontepadrao
        self.nome.pack(side=LEFT)

    # ESTADO
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.ufLabel = Label(self.janela4, text="UF:            \n", font=self.fontepadrao)
        self.ufLabel.pack(side=LEFT)
        self.uf = Entry(self.janela4)
        self.uf["width"] = 28
        self.uf["font"] = self.fontepadrao
        self.uf.pack(side=LEFT)

    # BOTÕES
        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8, font=self.fontebotao)
        self.inserir["text"] = "Inserir"
        self.inserir["width"] = 10
        self.inserir.pack(side=LEFT)
        self.inserir["command"] = self.inserirCidades

        self.alt = Button(self.janela8, font=self.fontebotao)
        self.alt["text"] = "Alterar"
        self.alt["width"] = 10
        self.alt.pack(side=LEFT)
        self.alt["command"] = self.alterarCidades

        self.excluir = Button(self.janela8, font=self.fontebotao)
        self.excluir["text"] = "Excluir"
        self.excluir["width"] = 10
        self.excluir.pack(side=LEFT)
        self.excluir["command"] = self.excluirCidades

        self.voltar = Button(self.janela8, font=self.fontebotao)
        self.voltar["text"] = "Voltar"
        self.voltar["width"] = 10
        self.voltar["command"] = self.janela.quit
        self.voltar.pack(side=LEFT)

        self.relatorio = Button(self.janela8, font=self.fontebotao)
        self.relatorio["text"] = "Gerar Relatório"
        self.relatorio["width"] = 20
        self.relatorio["command"] = self.gerarRelatorioPDF
        self.relatorio.pack(side=LEFT)

    # LABEL DE MENSAGENS
        self.mensagemLabel = Label(master, text="", font=self.fontepadrao)
        self.mensagemLabel.pack(pady=10)

    # TREEVIEW para exibir informações da cidade buscada
        self.tree_frame = Frame(master)
        self.tree_frame.pack(pady=10)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Nome", "UF"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome da Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.pack()

    # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def atualizarTabela(self):
        cid = Cidades()
        cidades = cid.selectAllCids()
        self.tree.delete(*self.tree.get_children())
        for c in cidades:
            self.tree.insert("", "end", values=(c[0], c[1], c[2]))

    def buscarCidades(self):
        cid = Cidades()
        idcidades = self.id.get()
        cid.selectCid(idcidades)

        if cid.idcidades:  #verifica se o ID foi encontrado e atribuído
            self.id.delete(0, END)
            self.id.insert(INSERT, cid.idcidades)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, cid.nome)
            self.uf.delete(0, END)
            self.uf.insert(INSERT, cid.uf)
        self.atualizarTabela()

    def inserirCidades(self):
        cid = Cidades()
        cid.nome = self.nome.get()
        cid.uf = self.uf.get()
        status = cid.insertCid()
        self.mensagemLabel["text"] = status
        self.limparCampos()
        self.atualizarTabela()

    def alterarCidades(self):
        cid = Cidades()
        cid.idcidades = self.id.get()
        cid.nome = self.nome.get()
        cid.uf = self.uf.get()
        status = cid.updateCid()
        self.mensagemLabel["text"] = status
        self.limparCampos()
        self.atualizarTabela()

    def excluirCidades(self):
        cid = Cidades()
        cid.idcidades = self.id.get()
        status = cid.deleteCid()
        self.mensagemLabel["text"] = status
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.uf.delete(0, END)

    def gerarRelatorioPDF(self):
        cid = Cidades()
        cidades = cid.selectAllCids()

        pdf_file = "relatorio_cidades.pdf"

        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)

        c.drawString(72, 750, "Relatório de Cidades")

        y_position = 725
        for cidade in cidades:
            c.drawString(72, y_position, f"ID: {cidade[0]} | Nome: {cidade[1]} | UF: {cidade[2]}")
            y_position -= 15
            if y_position < 72:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = 750

        c.save()
        messagebox.showinfo("Sucesso", "Relatório PDF gerado com sucesso.")


root = Tk()
Cidade(root)
root.state("zoomed")  # para a tela sempre aparecer maximizada
root.mainloop()
