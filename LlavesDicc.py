"""
Define una función la cual nos permita conocer todas las llaves dentro de un diccionario. La función debe cumplir con los siguientes requerimientos.

La función debe tener por nombre sequences_items.
La función debe recibir como argumento un diccionario.
La función deberá imprimir en consola cada una de la llaves dentro del diccionario."""

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 

def sequences_items(my_dict):
    x = my_dict.items()
    print(x)

sequences_items(my_dict)    


