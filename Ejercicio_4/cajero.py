print("----------------------")
print("------CAJERO----------")
print("----------------------")

CB10 = 0
CB2 = 0
CM = 0
Ch=int(input("Ingrese el valor del cheque: "))

while Ch != 0:
    B10 = Ch // 10000
    D = Ch - (B10*10000)
    B2 = D // 2000
    D = D - (B2*2000)
    M1 = D // 100
    CB10 = CB10 + B10
    CB2 = CB2 + B2
    CM = CM + M1

    print("Para el cheque de valor",Ch,"se dieron")
    print(B10,"billetes de $10.000")
    print(B2,"billetes de $2.000")
    print(M1,"monedas de $100")
    Ch = int(input("Ingrese el valor del cheque: "))

print("Los billetes de $10.000 que se usaron fue: "+str(CB10))
print("Los billetes de $2.000 que se usaron fue: "+str(CB2))
print("Las monedas de $100 que se usaron fue: "+str(CM))
