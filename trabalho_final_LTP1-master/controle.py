from janela_principal_2 import Janela_Principal
from tkinter import *
from bd_simulado import Bd_Simulado
class Controle:
    def __init__(self):
        self.bd = Bd_Simulado()
        self.bd.carregar_carros()
        self.bd.carregar_compradores()
        self.bd.carregar_vendedores()
        self.jn = Janela_Principal(self)
        for c in self.jn.grid_slaves():
            if type(c) is Button:
                print(c['text'])
        self.jn.mainloop()