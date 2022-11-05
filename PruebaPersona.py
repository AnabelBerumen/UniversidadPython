from Persona import Persona

print('Creacion de objetos'.center(50, '-'))
persona1 = Persona('karla', 'gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(50, '-'))
del persona1
