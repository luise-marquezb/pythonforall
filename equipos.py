import matplotlib.pyplot as plt

equipos = 4
juegos = 4
promedio = [0,0,0,0]
equipomin = equipomax = 0
equiposn = [1,2,3,4]

matriz = [[0,4,2,1], 
          [5,0,1,3],
          [0,2,0,2],
          [1,0,2,0]
          ]
         
print("%10s"%"Equipo", end="   ")
print("%10s"%"Juego 1", end="   ")
print("%10s"%"Juego 2", end="   ")
print("%10s"%"Juego 3", end="   ")
print("%10s"%"Juego 4", end="   ")
print("%10s"%"Goles")

for i in range(equipos):  # se repite 4 veces
    print("%10s"%equiposn[i], end="   ")
    for j in range(juegos):
        print("%10s"%"{0:.0f}".format(matriz[i][j]), end=" ")
        promedio[i] =  promedio[i] + matriz[i][j]
    print((promedio[i]), end=" ")  
    print()

maximo= minimo = promedio[0]

for x in range(0, 4):
    if((promedio[x]) > maximo):
       maximo = promedio[x]
       equipomax = x 
    elif (promedio[x] < minimo):
       minimo = promedio[x]
       equipomin = x
print()
       

print("El equipo con menos goles es el equipo #: -->",equipomin+1,"con -->", min(promedio), "goles")
print("El equipo con mas goles es el equipo #: -->", equipomax+1, "con -->", max(promedio), "goles")

fig, ax = plt.subplots()
ax.bar(promedio)
plt.show()

#print("El equipo con menos goles es: -->", min(promedio))