class Persona:
    contador_persona = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona {self.id_persona}[{self.nombre} {self.edad}]'


if __name__ == '__main__':
    p1 = Persona('Juan', 34)
    print(p1)
    p2 = Persona('Alex', 24)
    print(p2)
    p3 = Persona('Edu', 34)
    print(p3)

    print(f'Valor contador persona: {Persona.contador_persona}')
