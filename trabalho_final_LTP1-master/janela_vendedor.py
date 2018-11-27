from tkinter import *
from Vendedor import Vendedor
from tkinter import messagebox
class Janela_Vendedor(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Vendedor')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=10, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)

        self.btn_add = Button(self, text='Adicionar Vendedor', command=self.add_vend).\
            grid(row=4, column=1, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover Vendedor', command=self.rmv_vend).\
            grid(row=4, column=3, columnspan=2, pady=10, stick=S)
        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=5, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).\
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome').\
            grid(row=1, column=1, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var).\
            grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF').\
            grid(row=2, column=1, padx=1, pady=1)

        self.entry_mat_var = StringVar()
        self.entry_mat = Entry(self, textvariable=self.entry_mat_var).\
            grid(row=3, column=3, padx=1, pady=1)
        self.lbl_mat = Label(self, text='Matrícula').\
            grid(row=3, column=1, padx=1, pady=1)


    def add_vend(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        matricula = self.entry_mat_var.get()
        v = Vendedor(nome, cpf, matricula)
        self.control.bd.add_vendedor(v)
        messagebox.showinfo('Vendedor', f'{nome} foi adicionado.')

    def rmv_vend(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        matricula = self.entry_mat_var.get()
        rmvd = None
        if messagebox.askyesno('Excluir', f'Tem ceteza que deseja excluir o vendedor {nome}?') is False:
            return None
        for v in self.control.bd.show_vend():
            if v.get_nome() == nome and v.get_cpf() == cpf and v.get_matricula() == matricula:
                rmvd = self.control.bd.rmv_vend(v)
                messagebox.showinfo('Vendedor', f'{nome} foi removido.')
        if rmvd is None:
            messagebox.showerror('Vendedor', 'Não há vendedor cadastrado com estes dados')

    def destroy(self):
        self.control.bd.save_vendedor()
        super().destroy()