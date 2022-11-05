def suma(*args):
    res = 0

    for valor in args:
        res += valor
    return res


print(suma(4,6,8,1))

def mult(*args):
    res = 1

    for valor in args:
        res *= valor

    return  res


print(mult(2,2))

# recibir diccionario
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listarTerminos(ADA="Ada Lovelace", BTC="bitcoin")


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f"El factorial es {resultado}")

print("###")
def recursiva(num):
    if num >=1:
        print(num)
        recursiva(num -1)
    elif num == 0:
        return
    elif num <= 0:
        print('valor incorrecto')


num = -5
recursiva(num)

