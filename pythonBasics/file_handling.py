# Pregunta 2: Manejo de Archivos (Día a día)
# En nuestros proyectos frecuentemente procesamos archivos CSV. ¿Cómo leerías este archivo y extraerías información?

# archivo: ventas.csv
# fecha,producto,cantidad,precio
# 2024-01-15,Laptop,2,15000
# 2024-01-16,Mouse,5,500

# Tarea: Calcular el total de ventas por producto

import csv

ventas_por_producto = {} # Se declara el diccionario de ventas por producto, el key será el producto y el value será el total de ventas de este.

with open('ventas.csv', 'r') as archivo: # Se abre el archivo ventas.csv en modo de lectura 'r' y se devuelve como objeto "archivo" hasta salir del bloque with.
    reader = csv.DictReader(archivo) # DictReader es una clase del módulo csv, lee cada fila del csv y las convierte en diccionarios, usando los encabezados como claves.
    for fila in reader: # Itera sobre cada fila producida por DictReader
        producto = fila["producto"]
        total = int(fila['cantidad']) * float(fila['precio']) # Calcula el total de ventas del producto de la , convirtiendo los strings a int y float.

        # Si el producto ya se encuentra en el diccionario, sumamos su total. Si no lo está, lo inicializamos con el total inicial.
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += total 
        else:
            ventas_por_producto[producto] = total


print(ventas_por_producto)


        



    
