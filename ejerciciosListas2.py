""" Leer un arreglo A[ ] de enteros de tamaño n, donde n es ingresado
por el usuario, y posteriormente llenar un 
arreglo B[ ] con los valores de A[ ]. Visualizar el arreglo B[ ] en pantalla.
Por ejemplo: sea n = 5, A[ ] = {10, 2, 3, 5, 7}, 
 B[ ] seria, B[ ] = {10, 2, 3, 5, 7} """
 
"""  
datos= int(input("digite los datos: "))
arregloA= []
arregloB=[]
for i in range(datos):
    valores= int(input("digite los valores del arreglo: "))
    arregloA.append(valores)

for i in arregloA:
    arregloB.append(i)
    
print(arregloA)
print(arregloB) """



#///// ejercicio 6
""" 
Leer un arreglo A[ ] de enteros de tamaño n, donde n 
es ingresado por el usuario, y posteriormente llenar un 
arreglo B[ ] con los valores de A[ ] en forma inversa 
(de atrás hacia adelante). Visualizar el arreglo B[ ] en 
pantalla.
Por ejemplo: sea n = 5, A[ ] = {10, 2, 3, 5, 7}, 
 B[ ] seria, B[ ] = {7, 5, 3, 2, 10} """
 
 
""" datos= int(input("digite los datos: "))
arregloA= []
arregloB=[]
for i in range(datos):
    valores= int(input("digite los valores del arreglo: "))
    arregloA.append(valores)

for i in range(datos-1,-1,-1):
    arregloB.append(arregloA[i])

    
print(arregloA)
print(arregloB) """
    
#invirtiendo listas
""" 

lista1= [2,5,6,7,8,9,10]
lista=[]

for i in range(len(lista1)-1,-1,-1):
    lista.append(lista1[i])
    
print(lista)
  """
  
  
#///////////ejercicio 7
""" Llenar un arreglo A[ ] de tamaño n, donde
n es ingresado por el usuario, con los primeros n números pares.
Visualizar el arreglo A[ ] en pantalla.
Por ejemplo: sea n = 5, A[ ] = {2, 4, 6, 8, 10} """
""" 

tamaño_arreglo= int(input("tamaño del arreglo: "))
arreglo_a=[]
datos= 0
for i in range(1,tamaño_arreglo+1):
    datos +=2
    arreglo_a.append(datos)
print(arreglo_a) """


#//////////////////ejercicio 8
""" Leer dos rangos de valores y almacenar en un arreglo A[ ]
los cuadrados de los números comprendidos en el 
rango leído. Visualizar el arreglo A[ ] en pantalla.
Por ejemplo: sea rangoInf = 5, ranfoSup = 10, A[ ] = {25, 36, 49, 64, 81, 100} """
""" 
rangoInf= int(input("rango a empezar: "))
ranfoSup= int(input("digite hasta que numero hacer: "))
A=[]
for i in range(rangoInf,ranfoSup+1):
    i*=i
    A.append(i)
print(A) """

#////// ejercicio 9////

"""  Llenar un arreglo A[ ] de enteros de tamaño n, 
 donde n es ingresado por el usuario, con los resultados de una 
tabla de multiplicar de un numero X hasta n. X es ingresado por el usuario.
Por ejemplo: sea x = 3 y n = 5. 
Entonces A [ ] = {3, 6, 9, 12, 15} """
""" tabla= int(input("que tablas deseas saber: "))
rangoInf= int(input("hasta que numero deseas saber: "))
arreglo_a= []
for i in range(1,rangoInf+1):
    resultado= tabla*i
    arreglo_a.append(resultado)
    
print(arreglo_a) """


#//////////////////// ejercicio 10//
""" Leer n números por teclado, donde n es ingresado por el usuario. La mitad de los números ingresados se 
almacenara en un arreglo A[ ], y la otra mitad en un arreglo B[ ]. Finalmente almacenar todos los números de 
A[ ] y B[ ] en un arreglo C[ ]. Visualizar los arreglo A[ ], B[ ] y C[ ] en pantalla.
Por ejemplo: sea n = 5, los valores ingresados son: 10, 2, 3, 5, 7
A[ ] = {10, 2, 3}, B[ ] = {5, 7} y C[ ] = {10, 2, 3, 5, 7} """


""" n= int(input("cantidad de datos: "))
arreglo_a=[]
arreglo_b=[]
arreglo_c=[]
for i in range(n):
    datos=int(input("digite los valores a guardar: "))
    if i < n/2:
        arreglo_a.append(datos)
    else:
        arreglo_b.append(datos)
    arreglo_c.append(datos)
    
print(arreglo_a)
print(arreglo_b)
print(arreglo_c)
     """

#//// ejercicio 11////////////
""" Leer n números por teclado, donde n es ingresado 
por el usuario. Los valores pares se almacenaran en un 
arreglo A[ ], y los valores impares en un arreglo B[ ]. A[ ] y B[ ] 
deben quedar de tamaño exacto, de acuerdo 
a la cantidad de pares e impares respectivamente. Visualizar los arreglo A[ ] y B[ ] en pantalla.
Por ejemplo: sea n = 5, los valores ingresados son: 10, 2, 3, 5, 7
A[ ] = {10, 2} y B[ ] = {3, 5, 7} """


""" 
datos= int(input("digite los datos: "))
arreglo_a= []
arreglo_b= []

for i in range(datos):
    valores= int(input("escriba los valores: "))
    if valores%2==0:
        arreglo_a.append(valores)
    else:
        arreglo_b.append(valores)
        
print(arreglo_a)
print(arreglo_b) """



#/////////////////12

""" Leer dos arreglos A[ ] y B[ ] de tamaño n y m 
respectivamente y posteriormente crear un tercer arreglo C[ ]
que almacene los elementos de A[ ] y B[ ].
Por ej: A = [0, 1, 2, 3]
 B = [4, 5, 6, 7, 8, 9]
 C = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 """
 
""" n= int(input("escriba la cantidad del primer arreglo: "))
m=int(input("escribar la cantidad del segundo arreglo: "))
arreglo_a=[]
arreglo_b=[]
arreglo_c=[]

for i in range(n):
    datos=int(input("escriba los datos: "))
    arreglo_c.append(datos)
    
for i in range(m):
    datos=int(input("escriba los daots en: "))
    arreglo_c.append(datos)
    
print(arreglo_c)    
     """

#///////////////////13///////

#pop elimina el indice que se coloque en casoo que no se coloque indice
#elimina el ultimo de la lista
""" fila= [1,2,3,4,5,6,7,8,9,0,0,0]
for i in range(10):
    resultado= fila.pop(0)
    fila.append(resultado)
    print(fila)
  """
  
  
#dado un arreglo de numeros enteros eliminar los repetidos no se vale usar set
#remove()solo elimina la primera aparicion del elemento en la lista, sino hay ninguno marca error

#hacerlo de tres formas distintas

#//////// primera forma
lista1= [1,2,22,2,4,5,1,1,22,4,5,5,8,5]
tamaño_arreglo=len(lista1)
for i in range(tamaño_arreglo):
    valor= i+1
    while valor < tamaño_arreglo:
        if lista1[i]== lista1[valor]: 
            lista1.pop(valor)
            tamaño_arreglo-=1
            continue
        valor+=1
print(lista1)

#///////////////// segunda forma
lista2= []
for i in range(len(lista1)):
    if lista1[i] not in lista2:
        lista2.append(lista1[i])
print(lista2)



#////////////// diccionario
diccionario=dict()

for i in lista1:
    if i not in diccionario:
        diccionario[i]=1
print(list(diccionario.keys()))
