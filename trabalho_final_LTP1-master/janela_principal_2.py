from tkinter import *
from tkinter import messagebox
from janela_comprador import Janela_Comprador
from janela_vendedor import Janela_Vendedor
from janela_carros import Janela_Carros
class Janela_Principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        self.title('Concessionária')
        self.geometry('500x500+200+200')
        Label(self, text='Carros').grid(row=0, column=0, pady=5, columnspan=10, stick=N)

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy).\
            grid(row=100, column=0, padx=5, columnspan=4, pady=5, stick=S)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.menu = Menu(self)
        self.menucascata = Menu(self.menu, tearoff=0)
        self.menucascata.add_command(label='Vendedor', command=self.janela_vendedor)
        self.menucascata.add_command(label='Comprador', command=self.janela_comprador)
        self.menucascata.add_command(label='Carro', command=self.janela_carros)
        self.menucascata.add_separator()
        self.menucascata.add_command(label='Sair', command=self.destroy)
        self.menu.add_cascade(label='Menu', menu=self.menucascata)
        self.config(menu=self.menu)

        self.btn_atualizar_carros = Button(self, text='Atualizar Pátio', command=self.atualizar_patio).\
            grid(row=99, column=0, columnspan=10, pady=5)

        self.carregar_carros()

    def carregar_carros(self):
        r = 2
        c = 0
        for b in self.control.bd.show_carros():
            Button(self, width=10, text=f'{b.get_placa()}').grid(row=r, column=c, pady=5)
            c += 1
            if c == 4:
                c = 0
                r += 1

    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza que deseja sair?'):
            super().destroy()

    def janela_comprador(self):
        Janela_Comprador(self)

    def janela_vendedor(self):
        Janela_Vendedor(self, self.control)

    def janela_carros(self):
        Janela_Carros(self, self.control)

    def atualizar_patio(self):
        for c in self.grid_slaves():
            if type(c) is Button:
                if c['text'] != 'Atualizar Pátio' and c['text'] != 'Sair':
                    c.destroy()
        self.carregar_carros()
