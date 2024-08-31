

#end= " " da un espacio y evita el salto de linea
#el print() que esta vacio nos da el salto de linea
""" matrix= [[1,2,3],[4,5,6],[7,8,9]]

for i in matrix:
    for j in i:
        print(j, end= " ")
    print() """

    
#pedir al usuario los valores de la matrix y mostraselos organizados en forma de matrix
""" filas= int(input("cantidad de filas: "))
columnas= int(input("cantidad columnas: "))
matrix_completa= []
            
for i in range(filas):
    matrix= []
    for j in range(columnas):
        matrix.append( int(input("escriba los valores de la matrix: ")))
    matrix_completa.append(matrix)
        
for i in matrix_completa:
    for j in i:
        print(j, end= " ")
    print() """
    

#dada una matrix 3*3 sumar todos los valores de una esta
""" matrix= [[1,2,3],[4,5,6],[7,8,9]]
suma=0
for i in matrix:
    for j in i:
        suma+= j
print(suma) """

 
#///////////// que el profesor me explique esta       
#Transponer una matriz (Dada una matriz, genera su transpuesta (intercambiar filas y columnas).)
""" 
matrix= [[1,2,3],
         [2,5,6],
         [3,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[j][i], end= "")
    print() """
    
#hacer una cruz 

""" def figura1():
    tamaño_matrix= int(input("digite el tamaño de la matrix: "))
    while tamaño_matrix%2==0:
        tamaño_matrix= int(input("digite el tamaño de la matrix: "))
        
    for i in range(tamaño_matrix):
        for j in range(tamaño_matrix):
            if int(tamaño_matrix/2)==j:
                print("*", end= " ")
            elif int(tamaño_matrix/2)== i:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        print()
    print(tamaño_matrix)
figura1()   """ 

def figura1(tamaño_matrix):

        
    for i in range(tamaño_matrix):
        for j in range(tamaño_matrix):
            if int(tamaño_matrix/2)== i or int(tamaño_matrix/2)== j :
                print("*", end= " ")
            else:
                print("+", end=" ")
            
        print()
figura1(7)  

