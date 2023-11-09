alumnos = 10
examen = 3
promedio = [0,0,0,0,0,0,0,0,0,0]

matriz = [[5,6,7], 
          [8,5,6],
          [4,3,9],
          [1,2,3], 
          [4,5,6],
          [7,8,9],
          [5,6,3], 
          [4,5,9],
          [7,8,9],
          [1,2,3]]

print("%10s"%"Alumno", end="   ")
print("%10s"%"Nota 1", end=" ")
print("%10s"%"Nota 2", end=" ")
print("%10s"%"Nota 3", end=" ")
print("%10s"%"Promedio")

for i in range(alumnos):  # se repite 10 veces
    print("%10s"%i, end="   ")
    for j in range(examen): # se repite 3 veces
        print((matriz[i][j]), end=" ")   
        promedio[i] =  promedio[i] + matriz[i][j]
    promedio[i] =  promedio[i] / 3 
    print((promedio[i]), end=" ")  

    print()

    
