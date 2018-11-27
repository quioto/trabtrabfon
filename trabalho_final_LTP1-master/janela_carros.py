from tkinter import *
from carro import Carro
from tkinter import messagebox
class Janela_Carros(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Carros')
        self.geometry('250x250+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)

        self.btn_add = Button(self, text='Adicionar carro', command=self.add_car).\
            grid(row=7, column=1, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover carro', command=self.rmv_car).\
            grid(row=7, column=3, columnspan=2, pady=10, stick=S)

        self.btn_close = Button(self, text='Fechar janela', command=self.destroy, width=7)
        self.btn_close.grid(row=50, column=1, columnspan=3, stick=S, pady=20)

        self.entry_mod_var = StringVar()
        self.entry_mod = Entry(self, textvariable=self.entry_mod_var).\
            grid(row=1, column=3)
        self.lbl_mod = Label(self, text='Modelo').\
            grid(row=1, column=1, stick=E)

        self.entry_marca_var = StringVar()
        self.entry_marca = Entry(self, textvariable=self.entry_marca_var).\
            grid(row=2, column=3)
        self.lbl_mod = Label(self, text='Marca').\
            grid(row=2, column=1, stick=E)

        self.entry_ano_var = StringVar()
        self.entry_ano = Entry(self, textvariable=self.entry_ano_var).\
            grid(row=3, column=3)
        self.lbl_ano = Label(self, text='Ano').\
            grid(row=3, column=1, stick=E)

        self.entry_preco_var = StringVar()
        self.entry_preco = Entry(self, textvariable=self.entry_preco_var).\
            grid(row=4, column=3)
        self.lbl_preco = Label(self, text='Preço de Compra').\
            grid(row=4, column=1, stick=E)

        self.entry_estado_var = StringVar()
        self.entry_estado = Entry(self, textvariable=self.entry_estado_var).\
            grid(row=5, column=3)
        self.lbl_estado = Label(self, text='Estado').\
            grid(row=5, column=1, stick=E)

        self.entry_placa_var = StringVar()
        self.entry_placa = Entry(self, textvariable=self.entry_placa_var).\
            grid(row=6, column=3)
        self.lbl_placa = Label(self, text='Placa').\
            grid(row=6, column=1, stick=E)

    def add_car(self):
        modelo = self.entry_mod_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = self.entry_preco_var.get()
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        c = Carro(modelo, marca, ano, estado, preco, placa)
        self.control.bd.add_carro(c)
        messagebox.showinfo('Carro', f'{placa} foi adicionado.')

    def rmv_car(self):
        modelo = self.entry_mod_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = self.entry_preco_var.get()
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        rmvd = None
        if messagebox.askyesno('Excluir', f'Tem ceteza que deseja excluir o carro: {placa}?') is False:
            return None
        for c in self.control.bd.show_carros():
            if c.get_modelo() == modelo and c.get_marca() == marca and c.get_ano() == ano and c.get_placa() == placa:
                rmvd = self.control.bd.rmv_car(c)
                messagebox.showinfo('Carro', f'{placa} foi removido.')
        if rmvd is None:
            messagebox.showerror('Carro', 'Não há carro cadastrado com estes dados.')

    def destroy(self):
        self.control.bd.save_carros()
        self.control.jn.atualizar_patio()
        super().destroy()
