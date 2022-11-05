from Leccion10.mundo_pc.computadora import Computadora
from Leccion10.mundo_pc.monitor import Monitor
from Leccion10.mundo_pc.raton import Raton
from Leccion10.mundo_pc.teclado import Teclado
from Leccion10.orden import Orden

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    raton1 = Raton('HP', 'USB')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)

    teclado2 = Teclado('DELL', 'USB')
    monitor2 = Monitor('DELL', 15)
    raton2 = Raton('DELL', 'USB')
    computadora2 = Computadora('DELL', monitor2, teclado2, raton2)

    computadoras1 = [computadora1, computadora2]
    orden1 = Orden(computadoras1)
    print(orden1)