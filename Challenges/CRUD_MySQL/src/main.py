#import pymysql #Arreglar: conexion fallida
#miConexion = pymysql.connect(host="localhost", user="root", passwd= "Contravlady97", database="challengecrud")

from pydoc import text
import pyodbc
db = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=DESKTOP-4CUGQV7;DATABASE=Productos;UID=sa;PWD=contravlady')

txt = """
******************
     C R U D

    1 - Create
    2 - Remove
    3 - Update
    4 - Delete

******************
"""
def Create():
    name = input("Ingrese detalle: ")
    price = int(input("Ingrese precio"))

    cursor.execute("INSERT CrudPyWombat VALUES(%s, %s):")

Create()
cursor = db.cursor()
cursor.execute("SELECT count(*) FROM CrudPyWombat")

valor = cursor.fetchval()

print(valor)

