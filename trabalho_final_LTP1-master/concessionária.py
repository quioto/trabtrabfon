class Concessionaria:
    def __init__(self):
        self.carros = []

    def get_carros(self):
        return self.carros

    def add_carro(self, carro):
        # file = open(f'{self.nome}.txt', 'w')
        self.carros.append(carro)
        # file.writelines(str(self.carros) + '\n')
        # file.close()

    def save_cars(self):
        file = open('Concessionária.txt', 'w')
        for c in self.carros:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()