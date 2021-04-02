"""
Desarrolla un programa en Python que nos permita conocer todas las 
vocales que existen dentro de una palabra.

Requerimentos:

El usuario podrá ingresar, vía teclado, una palabra o sentencia de 
la cual quiera conocer todas sus vocales.
Todas las vocales deberán imprimirse en una sola línea.
Ejemplo.

>>> Ingresa una palabra/sentencia: 'PyWombat'
oa
"""

#Palabra = input("Ingresa una palabra: ")
#MinPalabra = Palabra.lower()
#print(MinPalabra)

palabra = "Eduardo"

reduPalabra = palabra.lower()

siHay = []

for i in reduPalabra:
    if i == "a":
        siHay = siHay + [i]
    if i == "e":
        siHay = siHay + [i]
    if i == "i":
        siHay = siHay + [i]
    if i == "o":
        siHay = siHay + [i]
    if i == "u":
        siHay = siHay + [i]


print(siHay)

""" #Codigo de tercero
palabra = input('Ingresa una palabra en minúscula: ')

vocales = ['a','e','i','o','u']

letras = []

for vocal in palabra.lower():
    if vocal in vocales:
        letras.append(vocal)

print(letras)
"""
