""" MSS001 Sistema para guardar e recuperar dados """
# IMPORTAÇÕES
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


def MSS01():
    # FUNÇÕES
    """
    def db001():
        conn = sqlite3.connect('cadastro.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome TEXT,'
                'endereco TEXT'
                'email TEXT'
                'telefone TEXT'
            ')')
    """

    def add_cliente():
        conn = sqlite3.connect('cadastro.db')
        c = conn.cursor()
        id = e_id.get()
        nome = e_nome.get()
        endereco = e_end.get()
        email = e_email.get()
        telefone = e_tel.get()
        if id != "" and nome !="" and endereco != "" and email !="" and telefone !="":
            c.execute("INSERT INTO clientes (id, nome, endereco, email, telefone) VALUES (?,?,?,?,?)",
                      (id, nome, endereco, email, telefone))
            conn.commit()
            messagebox.showinfo('Sucesso', 'Cliente adicionado com sucesso!')
            e_id.delete(0, END)
            e_nome.delete(0, END)
            e_end.delete(0, END)
            e_email.delete(0, END)
            e_tel.delete(0, END)

        else:
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')

    def buscar():
        bus01 = e_nome.get()
        conn = sqlite3.connect("cadastro.db")
        c = conn.cursor()

        c.execute("SELECT * FROM clientes")
        c_texto = c.fetchall()
        for linha in c_texto:
            identificador, nome, endereco, email, telefone = linha
            if bus01 == nome:
                e_id.insert(0, identificador)
                e_end.insert(0, endereco)
                e_email.insert(0, email)
                e_tel.insert(0, telefone)

    def deletar():
        id = e_id.get()
        conn = sqlite3.connect("cadastro.db")
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (id,))
        conn.commit()
        messagebox.showinfo('Sucesso', 'Cliente deletado com sucesso!')
        e_id.delete(0, END)
        e_nome.delete(0, END)
        e_end.delete(0, END)
        e_email.delete(0, END)
        e_tel.delete(0, END)

    def novo():
        app.destroy()
        MSS01()


    # TELA
    app = tk.Tk()
    app.geometry('1200x600+80+30')
    p1 = PhotoImage(file='img/logo3.png')
    app.iconphoto(False, p1)
    app.title('MSS001 - v1.0.2023')
    app['bg'] = "#1e3743"

    # TEXTOS
    l0 = Label(app, text="MSS001 CADASTRO DE CLIENTES", bg="#1e3743", fg="#FF6600", font=('Garamond 35'))
    l0.place(relx=0.2, rely=0.05)
    l1 = Label(app, text="ID", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    l1.place(relx=0.252, rely=0.25)
    l2 = Label(app, text="NOME ", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    l2.place(relx=0.22, rely=0.35)
    l3 = Label(app, text="ENDEREÇO ", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    l3.place(relx=0.178, rely=0.45)
    l4 = Label(app, text="EMAIL ", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    l4.place(relx=0.218, rely=0.55)
    l5 = Label(app, text="TELEFONE ", bg="#1e3743", fg="#FFFFFF", font=('Garamond 15'))
    l5.place(relx=0.185, rely=0.65)

    l6 = Label(app, text="Powered by MAGNA SOFTWARES SOLUTIONS", bg="#1e3743", fg="#FF6600", font=('Garamond 10'))
    l6.place(relx=0.4, rely=0.95)


    # ENTRADAS
    e_id = Entry(app, width=20, font=('Garamond 15'))
    e_id.place(relx=0.30, rely=0.25, relheight=0.04)
    e_nome = Entry(app, width=60, font=('Garamond 15'))
    e_nome.place(relx=0.30, rely=0.35, relheight=0.04)
    e_end = Entry(app, width=60, font=('Garamond 15'))
    e_end.place(relx=0.30, rely=0.45, relheight=0.04)
    e_email = Entry(app, width=60, font=('Garamond 15'))
    e_email.place(relx=0.30, rely=0.55, relheight=0.04)
    e_tel = Entry(app, width=60, font=('Garamond 15'))
    e_tel.place(relx=0.30, rely=0.65, relheight=0.04)
    a = e_nome.get()
    # BOTÕES
    # Salvar
    btn1 = Button(app, command=add_cliente)
    photo = tk.PhotoImage(file='img/salvar.png').subsample(3, 3)
    btn1.config(image=photo)
    btn1.imagem = photo
    btn1.place(relx=0.3, rely=0.75, relwidth=0.05, relheight=0.1)
    # Buscar
    btn2 = Button(app, command=buscar)
    photo = tk.PhotoImage(file='img/buscar.png').subsample(3, 3)
    btn2.config(image=photo)
    btn2.imagem = photo
    btn2.place(relx=0.4, rely=0.75, relwidth=0.05, relheight=0.1)
    # Deletar
    btn3 = Button(app, command=deletar)
    photo = tk.PhotoImage(file='img/delete.png').subsample(3, 3)
    btn3.config(image=photo)
    btn3.imagem = photo
    btn3.place(relx=0.6, rely=0.75, relwidth=0.05, relheight=0.1)
    # Novo
    btn4 = Button(app, command=novo)
    photo = tk.PhotoImage(file='img/novo.png').subsample(3, 3)
    btn4.config(image=photo)
    btn4.imagem = photo
    btn4.place(relx=0.7, rely=0.75, relwidth=0.05, relheight=0.1)

    # FINAL
    app.mainloop()


if __name__ == '__main__':
    MSS01()
