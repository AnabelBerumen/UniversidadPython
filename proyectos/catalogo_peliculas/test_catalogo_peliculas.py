from proyectos.catalogo_peliculas.dominio.Pelicula import Pelicula
from proyectos.catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Película')
        print('2. Listar Película')
        print('3. Eliminar Película')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4):'))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None
else:
    print('Salimos del programa...')