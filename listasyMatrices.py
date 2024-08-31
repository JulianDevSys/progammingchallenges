#listas //////////////////////////////
""" 
nombres= ['julian', 'esteban', 'sergio Andres', 'luis Miguel']
edades= [19,19,29,30]

for nombre, edad in zip(nombres, edades) :
    print(f'{nombre} tiene {edad} años' )
 """
#////////////////////////// sumar elementos de dos listas

""" numeros= [1,2,3,4,5]
numeros2= [2,3,4,5,6]
suma= [numero1 + numero2 for numero1, numero2 in zip(numeros,numeros2)]
print(suma) """

#/////////////////////////matrices////////////////////////////////////////
#definimos las matrices, en este caso elejims matrices de 3x3
""" matriz1= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matriz2= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#donde se va a almacenar la suma que hagamos de la matrix
suma_matriz= []

#sumamos elemento por elemento de la matrix

for i in range(3):
    fila_suma= []
    for j in range(3):
        suma_elemento= matriz1[i][j] + matriz2[i][j]
        fila_suma.append(suma_elemento)
    suma_matriz.append(fila_suma)
        
for i in suma_matriz:  
    print(i)  """  
    
#////////////////////x con matrices/////
""" 
filas_matrix= int(input("cuantas filas y colmanas quiere que tenga: "))
matrix= []

for i in range(filas_matrix):
    unir_matrix= []
    for j in range(filas_matrix):
        if i==j or i + j== filas_matrix-1:
            unir_matrix.append("*") 
        else:
            unir_matrix.append("")
    matrix.append(unir_matrix)

for i in matrix:
    print(i)
 """
#///////////////// forma correcta de iterar listas usando enumerate ////
""" numeros= [1,2,3,4,5,6,'pablo']
for valores in enumerate(numeros):
    valor= valores[1]
    print(f"haciendo lo primero que se me vino a la mente: {valor}") """
#////////// recorrer diccionarios con bucles///////////

""" diccionario= {
    'nombre': "julian",
    'apellido': "castro",
    'edad': 19,
}
#item nos permite obetener tanto el valor como la llave
for usuario in diccionario.items():
    keys= usuario[0] #clave
    Value= usuario[1] #valor
    print(f'{keys} : {Value}') """
    
#/////////////////////////////////////////////////////////////////////

""" frutas = ['manzana','pera', 'banano', 'sandia', 'aguacate', 'piña','mango']
frutasFavoritas= []
for fruit in frutas:
    if fruit== 'aguacate':
        continue
    frutasFavoritas.append(fruit)
print(frutasFavoritas)
print('me gustan todas estas frutas')
 """
#//////////////////////////segunda forma de hacerla
""" frutas = ['manzana','pera', 'banano', 'sandia', 'aguacate', 'piña','mango']
#el primer fruit es la condicion que es lo quiere que traiga
frutas_favoritas = [ fruit for fruit in frutas if  fruit != 'aguacate']
print(frutas_favoritas)
 """








