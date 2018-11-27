class Carro:
    def __init__(self, modelo, marca, ano, estado, preco, placa):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.estado = estado
        self.placa = placa
        self.comprador = None
        self.vendedor = None

    def vender(self, comp, vend):
        self.vendedor = vend
        self.comprador = comp

    def get_modelo(self):
        return self.modelo

    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_estado(self):
        return self.estado

    def get_preco(self):
        return self.preco

    def get_placa(self):
        return self.placa

    def get_dados(self):
        return self.modelo, self.marca, self.ano, self.estado, self.preco, self.placa

    def get_venda(self):
        return f'Comprador: {self.comprador.get_nome()} / Vendedor: {self.vendedor.get_nome()}'