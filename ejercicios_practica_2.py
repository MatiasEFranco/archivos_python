# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    planilla_csv = open(archivo,'r')     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
    stock_productos = list(csv.DictReader(planilla_csv))
    stock_total = 0

    for producto in stock_productos:
        stock_total += int(producto['tornillos'])

    planilla_csv.close()

    print("La cantidad de tornillos en stock es ", stock_total)

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    cantidad_2_ambientes = 0
    cantidad_3_ambientes = 0

    with open (archivo,'r') as planilla_csv:     # Leemos todos los datos y los almaacenamos en una  lista de diccionarios
        stock_productos = list(csv.DictReader(planilla_csv))
    
    for i in range(len(stock_productos)):
        try:
            cantidad_ambientes = int(stock_productos[i].get('ambientes'))
            if cantidad_ambientes == 2:
                cantidad_2_ambientes +=1
       
            elif cantidad_ambientes == 3:
                cantidad_3_ambientes +=1

            elif cantidad_ambientes == None:
                print("error")
        except:
            print("Error, dato erroneo en el archivo fila", i)

    print("La cantidad de departamentso de 2 ambientes es ", cantidad_2_ambientes)
    print("La cantidad de departamentso de 3 ambientes es ", cantidad_3_ambientes)

    planilla_csv.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
