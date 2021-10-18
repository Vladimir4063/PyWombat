"""
Ana necesita validar el correo en el login simple que está implementando para su plataforma.
Detalles:
Verifica solamente que este contenga @ y punto.
En la salida debe mostrar al usuario ¡Es válido! o No es válido!.
"""

correo = input('Ingresa el correo: ')

arroba = 0
puntos = 0
for i in correo:
    if i == '@':
        arroba = arroba + 1
    if i == '.':
        puntos = puntos + 1

if arroba == 1 and puntos >= 1:
    print("¡Es válido!")
else:
    print("¡No es válido!") 