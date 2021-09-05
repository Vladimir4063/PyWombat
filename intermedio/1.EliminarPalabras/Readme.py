
palabra = input("Introduce la palabra a eliminar: ")
#palabra = "Vladimir"

lista = []
with open('frankenstein.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        cnt = linea.split() #Split() crea una cadena en lista
        for i in cnt:
            if i != palabra:
                lista.append(i)
            else:    
                continue
    archivo.close()        
        

with open('newText.txt', 'w') as archivo1:
    archivo1.write(" ".join(lista)) #join crea una lista en cadena
    archivo1.close() 
print("ARCHIVO NUEVO CREADO")