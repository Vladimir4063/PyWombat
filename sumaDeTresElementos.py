print("Ingrese un numero para hacer la suma de Elementos X3.")

nro = int(input("ingrese un numero: "))

def elementosX3(nro):
    resultado = nro + (nro*nro) + ((nro*nro) * nro)
    return resultado

print(elementosX3(nro))