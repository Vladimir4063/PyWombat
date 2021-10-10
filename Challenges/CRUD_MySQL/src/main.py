#import pymysql #Arreglar: conexion fallida
#miConexion = pymysql.connect(host="localhost", user="root", passwd= "Contravlady97", database="challengecrud")

from pydoc import text
import pyodbc
# import sqlite3
# db_lite = ''

db = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-4CUGQV7;DATABASE=Productos;UID=sa;PWD=contravlady')
cursor = db.cursor()

def ViewProducts():
    try:
        query = "SELECT * FROM CrudPyWombat"
        cursor.execute(query)
        lista = cursor.fetchall()
        for i in lista:
            print(i)

    except Exception as ex:
        print(ex)

def Create():
    try:
        name = input("Ingrese detalle: ")
        price = int(input("Ingrese precio: "))
        query = "INSERT CrudPyWombat(Nombre, Precio) VALUES(?,?)"
        cursor.execute(query, name, price)
        cursor.commit()
        cursor.close()

    except Exception as ex:
        print(ex)

def Remove():
    
    try:
        ViewProducts()
        producDelete = input("Producto a eliminar: ")
        query = "DELETE FROM CrudPyWombat WHERE Nombre = ?"
        cursor.execute(query, producDelete)
        cursor.commit()
        filasAfectadas = cursor.fetchone()
        #filasAfectadas = abs(cursor.rowcount)

        if filasAfectadas > 0:
            print(filasAfectadas)
            print("Producto eliminado.") 
        else:
            print("Producto no encontrado.")

    except Exception as ex:
        print(ex)

txt = """
******************
     C R U D

    1 - Create
    2 - Remove
    3 - Update
    4 - Delete
    5 - Exit
"""
#Create()
Remove()
#ViewProducts()

# opc = 0
# while(opc != 5):
#     print(txt)
#     opc = int(input("Ingrese una opción: "))
#     if(opc == 1):
#         Create()
#     if(opc == 2):
#         Remove()