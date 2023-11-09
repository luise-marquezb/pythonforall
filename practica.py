
tablainicio= 1
tablafinal = 10
inicio=1
final=10

for x in range(tablainicio,tablafinal+1):  
    print("Tabla de multiplicar",x)
    for y in range(inicio,final+1):
        print((x,"x" ,y) , x * y )
    print()



