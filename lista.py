elementList = [1,2,3,4,5,6,7,8,9]
for item in elementList:
    print("Tabla de multiplicar",item)
    
numero= int (input("introduzca un numero: "))

for a in range(1,11):
    resultado=a*numero
    print(("%d x %d = %d") % (numero,a,resultado))

    