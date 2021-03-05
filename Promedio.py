"""Fernando y su grupo de amigo, alumnos de preparatoria, quiere conocer el promedio final de su semestre. Es por ello que en esta ocasión tendrás que crear un script el cual le permita, no solo a Fernando, si no a cualquier alumno de la preparatoria, conocer su promedio final.

El programa debe poseer las siguientes características.

El script debe ejecutarse una vez por usuario.
El script debe mostrar en consola el promedio del alumno.
Algo que debes tener en cuenta es que la preparatorio maneja un plan de estudio de 10 materias por alumnos.
"""

lstNotas = []

print("Ingresa 10 notas para obtener un promedio: ")
vuelta = 1

while vuelta <= 10:
    vuelta = vuelta + 1
    notas = int(input("Ingresar nota: "))
    lstNotas.append(notas)
    promedio = sum(lstNotas) / 10
    
print("Nota promedio: ", (promedio))


