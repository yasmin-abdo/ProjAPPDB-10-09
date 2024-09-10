import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import importlib


class Login:

    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x400")

        # imagem
        try:
            img = Image.open("image/Capturar.PNG")  # Caminho da imagem
            img = img.resize((300, 300))
            self.photo = ImageTk.PhotoImage(img)

            self.image_label = tk.Label(self.master, image=self.photo)
            self.image_label.pack(pady=20)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar a imagem: {e}")

        # usuário
        self.usuario_label = tk.Label(self.master, text="Usuário:")
        self.usuario_label["font"] = "Calibri", 13
        self.usuario_label.pack(pady=5)
        self.usuario = tk.Entry(self.master)
        self.usuario.pack(pady=5)
        self.usuario["font"]= "Calibri",13

        # senha
        self.senha_label = tk.Label(self.master, text="Senha:")
        self.senha_label["font"] = "Calibri", 13
        self.senha_label.pack(pady=5)
        self.senha = tk.Entry(self.master, show="*")
        self.senha.pack(pady=5)
        self.senha["font"] = "Calibri", 13

        # Botão de login
        self.login_button = tk.Button(self.master, text="Login", command=self.entrar)
        self.login_button.pack(pady=30)
        self.login_button["width"] = 15
        self.login_button["font"] = "Calibri", 13

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        # Autenticação
        if usuario == "adm" and senha == "123":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.master.destroy()  # Fecha a tela de login

            # Importa e inicia a tela principal
            try:
                principal = importlib.import_module('principal')
                principal.iniciar()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao abrir a tela principal: {e}")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = Login(master=root)
    root.mainloop()
