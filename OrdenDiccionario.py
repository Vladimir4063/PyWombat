"""
Desarrolla una función la cual nos permita crear un diccionario, a partir de los parámetros establecidos al momento de llamar a dicha función.

La función debe cumplir con los siguientes requerimientos.

° La función debe tener por nombre generate_dict.
° La función podrá recibir una n cantidad de parámetros.
° A partir de los parámetros recibidos, la función deberá retornar un nuevo diccionario.
° Las llaves del diccionario deberán encontrarse ordenados con respecto al orden de los parámetros ingresados.
>>> generate_dic(a='Primer elemento', b='Segundo elemento', c='Tercer elemento')
{
    'a': 'Primer elemento,
    'b': 'Segundo elemento',
    'c': 'Tercer elemento',
}
"""

from collections import OrderedDict
def generate_dict(a, b, c):
    return {
            'a': a,
            'b': b,
            'c': c
            }

print(generate_dict(a="Hola", b="Soy", c="Vlaidmir"))

#web
def generate_dict(**kwargs):
    return dict(OrderedDict(**kwargs))


print(generate_dict(nombre="Vladimir", apellido= "Gutierrez", edad = 23, calle = "V. Hugo", region= "Bs As", phone = 1231231))


def generate_dict(**kwargs):
    return kwargs

#print(generate_dict(first_key='a', second_key='b', last_key='z'))
#print(generate_dict(a='a', b='b', c='z'))
#print(generate_dict(a='Primer elemento', b='Segundo elemento', c='Tercer elemento'))
print(generate_dict(nombre="Vladimir", apellido= "Gutierrez", edad = 23, calle = "V. Hugo", region= "Bs As", phone = 1231231))
