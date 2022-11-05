from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.mostrar_detalles())


empleado = Empleado('Juan',5000)
imprimir_detalles(empleado)

gerente = Gerente('karla', 6000, 'Sistemas')
imprimir_detalles(gerente)