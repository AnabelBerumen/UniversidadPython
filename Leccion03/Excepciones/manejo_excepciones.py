from NumerosIdenticosException import NumerosIdenticosException
resultado = None


try:
    a = int(input('primer numero'))
    b = int(input('Segundo numero'))
    if a == b:
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrió un error {e}')
except TypeError as e:
    print(f'Ocurrió un error {e}')
except Exception as e:
    print(f'Ocurrió un error {e}')
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Ejecutando bloque finaly')

print(f'resultado {resultado}')
print('Continuamos ...')
