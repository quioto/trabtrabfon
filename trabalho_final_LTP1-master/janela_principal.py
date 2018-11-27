from tkinter import *
from tkinter import messagebox
from janela_comprador import Janela_Comprador
from janela_vendedor import Janela_Vendedor
from janela_carros import Janela_Carros
from janela_nome import Janela_Nome
class Janela_Principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        Janela_Nome(self)
        self.title(f'{Janela_Nome.nome}')
        self.geometry('250x250+200+200')
        Label(self, text='Menu').grid(row=0, column=0, pady=10, columnspan=3)
        self.btn_comprador = Button(self, width=10, text='Comprador',
                                    command=self.janela_comprador).grid(row=1, column=0, padx=5)
        self.btn_vendedor = Button(self, width=10, text='Vendedor',
                                   command=self.janela_vendedor).grid(row=1, column=1, padx=5)
        self.btn_Carros = Button(self, width=10, text='Carros',
                                 command=self.janela_carros).grid(row=1, column=2, padx=5)
        self.btn_close = Button(self, width=10, text='Sair',
                         command=self.destroy).grid(row=2, column=0, padx=5, columnspan=3, pady=5)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        r = 0
        c = 0
        for b in self.control.bd.carros:
            self.b_carro = Button(self, width=10, text=f'{b[5]}').grid(row=r, column=c)
            c += 1
            if c == 2:
                c = 0
                r += 1



    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza que deseja sair?'):
            super().destroy()

    def janela_comprador(self):
        Janela_Comprador(self)

    def janela_vendedor(self):
        Janela_Vendedor(self)

    def janela_carros(self):
        Janela_Carros(self)
