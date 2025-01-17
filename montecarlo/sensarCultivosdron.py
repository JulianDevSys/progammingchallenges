import random

valor_columnas= int(input("escriba el numero de columnas: "))
valor_filas= int(input("escriba el numero de filas: "))

def generarPlantacion(dimencion):
    plantacion1=[[5,3,2],
            [1,4,8],
            [2,3,1]]
    plantacion= []
    for i in range(dimencion[0]):
        fila= []
        for j in range(dimencion[1]):
            valores= random.randint(1,10)
            fila.append(valores)
        plantacion.append(fila)

    return plantacion1
        
        
def analizarDensidad(plantacion, limite=4):
    valor= generarPlantacion(plantacion)
    print(valor)
    matriz=[]
    for i in range(len(valor)):
        fila= []
        for j in range(len(valor[1])):
            if valor[i][j]< limite:
                fila.append("BAJO")
            else:
                fila.append("ALTO")
        matriz.append(fila)
            
    return matriz
#///////////////////////////////////////////////////////////////////////

def reporteCrecimento(plantacion):
    posiciones= []
    contador= 0
    contador2= 0
    promedios= []
    promedio_altos= 0
    promedio_bajos= 0
    surcos= 0
    posiocion=0
    valor= 0
    matrix_plantacion= generarPlantacion(plantacion)
    densidad_analizado= analizarDensidad(plantacion, limite=4)
    for i in range(len(matrix_plantacion)):
        
        for j in range(len(matrix_plantacion)):
            surcos+=matrix_plantacion[i][j]
            if valor < matrix_plantacion[i][j]:
                valor= matrix_plantacion[i][j]
                posiocion=j
        promedio= surcos / len(matrix_plantacion[i])
        valor= 0   
        posiciones.append(posiocion)
        promedios.append(promedio)
        promedio= 0
        surcos= 0
        
    for i in range(len(densidad_analizado)):
        for j in range(len(densidad_analizado)):
            if densidad_analizado[i][j]== "ALTO":
                contador+= 1
                promedio_altos+= matrix_plantacion[i][j]
            elif densidad_analizado[i][j]== "BAJO":
                contador2+= 1
                promedio_bajos+= matrix_plantacion[i][j]
    total1= promedio_altos/contador
    total2= promedio_bajos/contador2
    resultado= [total1, total2]
    return promedios,posiciones, resultado 




dimencion=[valor_columnas, valor_filas]

#print(analizarDensidad(dimencion))
#print(generarPlantacion(dimencion))
print(reporteCrecimento(dimencion))
