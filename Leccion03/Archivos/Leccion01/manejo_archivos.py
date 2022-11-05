try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('agregamos información al archivo\n')
    archivo.write('adios')
except Exception as e:
    print(e)
finally:
    archivo.close()