print("---------------------------------------------------")
print("---------------INVERSIÓN DE NÚMEROS ---------------")
print("---------------------------------------------------")

n = int(input("Digite un número entero positivo "))
inv = 0
if n >= 0:
    while n > 0:
        i = n % 10
        inv = inv * 10 + i
        n = n // 10
    print("El número invertido es " +str(inv))
else:
    print("El número que usted digitó es negativo")