class Aritmetica:
    """
    blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """
    def __init__(self,opA, opB):
        self.opA = opA
        self.opB = opB


    def sumar(self):
        return self.opA + self.opB

    def restar(self):
        return self.opA - self.opB

    def multiplicar(self):
        return self.opA * self.opB

    def dividir(self):
        return self.opA / self.opB


ar1 = Aritmetica(5,3)

print(f"Suma {ar1.sumar()}")
