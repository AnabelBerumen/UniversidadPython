from Leccion07.Orden import Orden
from Leccion07.Producto import Producto

producto1 = Producto('Camisa', 150)
producto2 = Producto('Pantalon', 200)
producto3 = Producto('Calcentines', 50)
producto4 = Producto('Blusa',70)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)

print(orden1)
print(f'Total ${orden1.calcular_total()}')
orden2 = Orden(productos2)
print(orden2)
print(f'Total ${orden2.calcular_total()}')
