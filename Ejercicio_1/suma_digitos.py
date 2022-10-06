print("--------------------------------------------------")
print("---------SUMA DE LOS DÍGITOS DEL n NÚMERO---------")
print("--------------------------------------------------")

n = int(input("Digite un número entero positivo "))
suma = 0
if n >= 0:
    while n != 0:
        suma = suma + (n % 10)
        n = n // 10
    print("La suma de los números es " +str(suma))
else:
    print("El número que usted digitó es negativo")

