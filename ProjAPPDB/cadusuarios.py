from tkinter import *
from tkinter import ttk
from usuarios import Usuarios
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox


class Usuario:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)
        self.janela.pack()

    # TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:")
        self.titulo["font"] = ("Calibri", "30", "italic", "bold")
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Usuários\n")
        self.titulo2["font"] = ("Calibri", "20", "italic")
        self.titulo2.pack()

    # IDUSUARIO
        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idLabel = Label(self.janela2, text="idUsuário:     \n", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 18
        self.id["font"] = self.fontepadrao
        self.id.pack(side=LEFT)

        self.buscar = Button(self.janela2, font=self.fontebotao)
        self.buscar["text"] = "Buscar"
        self.buscar["width"] = 10
        self.buscar.pack(side=LEFT)
        self.buscar["command"] = self.buscarUsuario

    # NOME
        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nomeLabel = Label(self.janela3, text="Nome:     \n", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3)
        self.nome["width"] = 30
        self.nome["font"] = self.fontepadrao
        self.nome.pack(side=LEFT)


    # TELEFONE
        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telLabel = Label(self.janela4, text="Telefone: \n", font=self.fontepadrao)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4)
        self.tel["width"] = 29
        self.tel["font"] = self.fontepadrao
        self.tel.pack(side=LEFT)

    # EMAIL
        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.emailLabel = Label(self.janela5, text="E-mail:    \n", font=self.fontepadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 30
        self.email["font"] = self.fontepadrao
        self.email.pack(side=LEFT)

    # USUARIO
        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuLabel = Label(self.janela6, text="Usuário:  \n", font=self.fontepadrao)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6)
        self.usu["width"] = 30
        self.usu["font"] = self.fontepadrao
        self.usu.pack(side=LEFT)

    # SENHA
        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senhaLabel = Label(self.janela7, text="Senha:    \n", font=self.fontepadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 30
        self.senha["font"] = self.fontepadrao
        self.senha["show"] = "*"  # pra não mostrar a senha
        self.senha.pack(side=LEFT)

    # BOTÕES
        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.inserir = Button(self.janela8, font=self.fontebotao)
        self.inserir["text"] = "Inserir"
        self.inserir["width"] = 10
        self.inserir.pack(side=LEFT)
        self.inserir["command"] = self.inserirUsuario

        self.alt = Button(self.janela8, font=self.fontebotao)
        self.alt["text"] = "Alterar"
        self.alt["width"] = 10
        self.alt.pack(side=LEFT)
        self.alt["command"] = self.alterarUsuario

        self.excluir = Button(self.janela8, font=self.fontebotao)
        self.excluir["text"] = "Excluir"
        self.excluir["width"] = 10  # largura
        self.excluir.pack(side=LEFT)
        self.excluir["command"] = self.excluirUsuario

        self.voltar = Button(self.janela8, font=self.fontebotao)
        self.voltar["text"] = "Voltar"
        self.voltar["width"] = 10  # largura
        self.voltar["command"] = self.janela.quit
        self.voltar.pack(side=LEFT)

        self.relatorio =  Button(self.janela8, font=self.fontebotao)
        self.relatorio["text"] = "Importar Relatório"
        self.relatorio["width"] = 20
        self.relatorio["command"] = self.gerarRelatorioPDF
        self.relatorio.pack(side=LEFT)

    # MENSAGEM
        self.mensagemLabel = Label(master, text="", font=("Arial", 14))
        self.mensagemLabel.pack(pady=10)

    #TREEVIEW
        self.tree = ttk.Treeview(master, columns=("ID", "Nome", "Telefone", "E-mail", "Usuário"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.pack()

    # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4]))

    def buscarUsuario(self):
        user = Usuarios()
        id = self.id.get()
        resultado = user.selectUser(id)
        if user.idusuario:
            self.id.delete(0, END)
            self.id.insert(INSERT, user.idusuario)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.tel.delete(0, END)
            self.tel.insert(INSERT, user.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, user.email)
            self.usu.delete(0, END)
            self.usu.insert(INSERT, user.usuario)
            self.senha.delete(0, END)
            self.senha.insert(INSERT, user.senha)
        self.mensagemLabel["text"] = resultado
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        resultado = user.insertUser()
        self.mensagemLabel["text"] = resultado
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        resultado = user.updateUser()
        self.mensagemLabel["text"] = resultado
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        resultado = user.deleteUser()
        self.mensagemLabel["text"] = resultado
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.tel.delete(0, END)
        self.email.delete(0, END)
        self.usu.delete(0, END)
        self.senha.delete(0, END)

    def gerarRelatorioPDF(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()

        pdf_file = "relatorio_usuarios.pdf"

        # Adiciona o título
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Adiciona os dados
        c.drawString(72, 750, "Relatório de Usuários")

        y_position = 725
        for u in usuarios:
            c.drawString(72, y_position, f"ID: {u[0]} | Nome: {u[1]} | Telefone: {u[2]} | E-mail: {u[3]} | Usuário: {u[4]}")
            y_position -= 15
            if y_position < 72:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = 750

        c.save()
        messagebox.showinfo("Sucesso", "Relatório PDF gerado com sucesso.")


root = Tk()
Usuario(root)
root.state("zoomed")  # para a tela sempre aparecer maximizada
root.mainloop()
