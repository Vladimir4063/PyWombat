#import pymysql #Arreglar: conexion fallida
#miConexion = pymysql.connect(host="localhost", user="root", passwd= "Contravlady97", database="challengecrud")

from pydoc import text
import pyodbc
# import sqlite3
# db_lite = ''

db = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-4CUGQV7;DATABASE=Productos;UID=sa;PWD=contravlady')
cursor = db.cursor()

def Read():
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
        

    except Exception as ex:
        print(ex)

def Update():
    try:
        Read()
        productUpdate = input("Producto a actualizar: ")
        newName = input("Nuevo nombre: ")
        newPrice = int(input("Nuevo precio: "))
        query = "UPDATE CrudPyWombat SET Nombre = ?, Precio = ? WHERE Nombre = ?"
        cursor.execute(query, newName, newPrice, productUpdate)
        cursor.commit()
        filasAfectadas = abs(cursor.rowcount)
        
        if filasAfectadas > 0:
            Read()
            print("Producto Actualizado.")
        else:
            Read()
            print("Producto no encontrado.")

    except Exception as ex:
        print(ex)

def Delete():
    try:
        Read()
        producDelete = input("Producto a eliminar: ")
        query = "DELETE FROM CrudPyWombat WHERE Nombre = ?"
        cursor.execute(query, producDelete)
        cursor.commit()
        filasAfectadas = abs(cursor.rowcount)

        if filasAfectadas > 0:
            Read()
            print("## Producto eliminado ##") 
        else:
            print("Producto no encontrado.")

    except Exception as ex:
        print(ex)

txt = """
******************
     C R U D

    1 - Read
    2 - Create  
    3 - Update
    4 - Delete
    5 - Exit
"""

opc = 0
while(opc != 5):
    print(txt)
    opc = int(input("Ingrese una opción: "))
    if(opc == 1):
        Read()
    if(opc == 2):
        Create()
    if(opc == 3):
        Update()
    if(opc == 4):
        Delete()