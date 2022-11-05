class MiClase:

    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(f'-metodo estatico- {MiClase.variable_clase}')

    @classmethod
    def metodo_clase(cls):
        print(f'-metodo_clase- {cls.variable_clase}')

    def metodo_instancia(self):
        print('-metodo_instancia-')
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

if __name__ == '__main__':
    print(MiClase.variable_clase)
    miClase = MiClase('valor variable de instancia')
    print(miClase.variable_instancia)
    print(miClase.variable_clase)

    MiClase.variable_clase2 = 'Valor variable clase 2'

    miClase2 = MiClase('otro valor de instancia')
    print(miClase.variable_instancia)
    print(miClase2.variable_clase)
    print(MiClase.variable_clase2)
    print(miClase.variable_clase2)
    print(miClase2.variable_clase2)
    MiClase.metodo_estatico()
    MiClase.metodo_clase()

    miObjeto1 = MiClase('variable_instancia')
    miObjeto1.metodo_clase()
    miObjeto1.metodo_instancia()
