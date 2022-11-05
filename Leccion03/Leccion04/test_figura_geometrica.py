from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calcular area cuadrado{cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, 4, 'azul')
print(f"Calcular area rectangulo {rectangulo1.calcular_area()}")
print(rectangulo1)
# MRO Method Resolution Order
print(Cuadrado.mro())

