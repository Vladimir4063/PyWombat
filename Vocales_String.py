#Desarrolla un programa que nos permita conocer todas las vocales que existen dentro de un string.
"""
El usuario podrá ingresar, vía teclado, una palabra o frase de su interés.
El programa deberá mostrar en consola todas las vocales presentes en el string ingresado.
En caso el string ingresado no posea vocales, el programa no deberá imprimir nada.

Las vocales son:
a: 2
e: 2
i: 0
o: 3
u: 1
"""

#mensaje = input("Ingresa una palabra: ")
palabra = "Est es na racin"
reduPalabra = palabra.lower()

siHay = []
a = 0
e = 0
i = 0
o = 0
u = 0

for v in reduPalabra:
    if v == "a":
        siHay = siHay + [v]
        a = a + 1 
    if v == "e":
        siHay = siHay + [v]
        e = e + 1
    if v == "i":
        siHay = siHay + [v]
        i = i + 1
    if v == "o":
        siHay = siHay + [v]
        o = o + 1
    if v == "u":
        siHay = siHay + [v]
        u = u + 1     
print(siHay)

if a > 0:
    print("A: ", a)
if e > 0:
    print("e: ", e)
if i > 0:
    print("I: ", i)
if o > 0:
    print("O: ", o)
if u > 0:
    print("U: ", u)