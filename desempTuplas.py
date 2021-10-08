from typing import Text


opc = 0
while opc != 4:
    txt = """
    1 - Banana
    2 - Manzana
    3 - Naranja
    4 - salir
    """
    print(txt)
    lista = ["Banana", "Manzana", "Naranja"]

    opc = int(input("Ingrese fruta: "))

    if opc == 1:
        print(lista[0])
    if opc == 2:
        print(lista[1])
    if opc == 3:
        print(lista[2])

