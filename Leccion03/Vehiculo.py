class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo color {self.color} con {self.ruedas}  ruedas'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()} velocidad {self.velocidad}'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} Tipo {self.tipo}'


if __name__ == '__main__':
    vehiculo = Vehiculo('Rojo', 4)
    coche = Coche('Azul', 4, 100)
    bici = Bicicleta('Gris', 2, 'toro')

    print(vehiculo)
    print(coche)
    print(bici)
