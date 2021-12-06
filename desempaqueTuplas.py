""""
Dada la siguiente tupla de elementos:

('Loki', 'Duke', 'Princesa', 'Lisa')
Desarrolla un script que nos permita -almacenar en variables- el primer, segundo y cuarto elemento.

Ejemplo.
>>> primer_elemento
Loki
>>> segundo_elemento
Duke
>>> cuarto_elemento
Lisa
Restricciones:

No es posible obtener los elementos por su índice.
"""

primer_elemento = input("Ingrese el primer elemento: ")
segundo_elemento = input("Ingrese el segundo elemento: ")
tercer_elemento = input("Ingrese el tecer elemento: ")

variables = []

variables.append(primer_elemento)
variables.append(segundo_elemento)
variables.append(tercer_elemento)

print("Tupla: ")
print(tuple(variables))
