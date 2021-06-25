year = int(input('Año: '))

if year % 4 == 0 and not year % 100 == 1:
    print('Año bisiestro!')
else:
    print('Año ordinario!')