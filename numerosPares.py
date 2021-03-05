num1 = int(input("Ingrese el valor X: "))
num2 = int(input("Ingrese el valor Y: "))


def rango_pares(num1, num2):
    if num1 < num2:
        num = num1                     
        for i in range(num1,num2):
            num = num + 2
            print(num, end=" ")
            if num >= num2:
                print("Fin del programa")
                break
        
    else:
        print("'Y' Debe ser mayor a 'X'")
        print("Fin del programa.")

        

rango_pares(num1,num2)