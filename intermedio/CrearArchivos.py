import os

#ruta = input("Ingrese una ruta, seguido del nombre del archivo: ")
ruta = '../eliminar/ArchivoCreado.txt'
archivo = open(str(ruta), "w")
archivo.write("Primera linea")
archivo.close
print("Archivo creado de forma exitosa")