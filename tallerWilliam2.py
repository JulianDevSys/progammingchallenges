"""  Escriba un programa que calcule la probabilidad de que el producto de
los puntos de tres lanzamientos de los dados sea menor que 50. """

""" 
def lanzamiento_dados():
    tiros= 0
    contador= 0
    for l in range(1,7):
        for j in range(1,7):
            for i in range(1,7):
                tiros+=1
                valor= i*j*l
                if valor < 50:
                    contador+=1
    pordentaje= contador/tiros*100       
    return f"veces que sale: {contador}, cantidad tiros: {tiros}, probabilidad: {pordentaje}"
print(lanzamiento_dados()) """
#producto cartesiano entre dos 
import itertools
import math
lista= [1,2,3,4,5,6]
count= 0
guardar= itertools.product(lista,repeat=3)
for i in guardar:
    if math.prod(i)<50:
        count+=1

print(count)

#ejercicio 2
""" Escriba un código para determinar en qué cuadrante se encuentra un
punto ingresado por teclado. """
""" 
def cuadrante(x,y):
    if x > 1 and  y >1:
        return "cuadrante 1"
    elif x  < 1 and y > 1:
        return "cuadrante 2"
    elif x < 1 and y < 1:
        return "cuadrante 3"
    else:
        return "cuadrante 4"
print(cuadrante(2,-1)) """


#Determine el número de formas en las que se puede vestir un joven si
#dispone de dos pares de zapatos, dos pantalones y tres camisas.
""" import itertools
def forma_vestir():
    contador= 0
    listas = [["zapato1", "zapato2"], ["pantalon1", "pantalon2"], ["camisa1", "camisa2", "camisa3"]]
    combinaciones = list(itertools.product(*listas))  
    print(combinaciones)
    for i in combinaciones:
        contador+=1
    return contador

print(forma_vestir()) """

#Ejemplo 3 . Escriba un código para determinar por enumeración 
# el espacio muestral del lanzamiento triple de un dado.
""" El resultado (fragmento) de la ejecución de este código es: 
    {(5 , 1, 6), (5, 3, 3), (5, 4, 2), (2 , 1, 6),
(1, 6, 6), (2, 2, 5), (6 , 6, 4), """

""" import itertools
def posibles_combinaciones(lista:list):
    valor= itertools.product(lista,repeat=3)
    for i in valor:
        print(i)
posibles_combinaciones([1,2,3,4,5,6]) """


#Escriba un código en Python para enumerar el evento 
#E = {puntaje menor que 4} a partir de su des cripción
#formal en el lanzamiento de un dado

#El resultado de la ejecución de este código es: E = {1, 2, 3}

""" lista= [1,2,3,4,5,6]
ejercicio4= map(lambda x: x ,filter(lambda x: x <4,lista))
print(list(ejercicio4))  """

# Escriba un código en Python para determinar los elementos de un evento si debe cumplir la
#condición que la suma de los puntos en dos lanzamientos de un dado no sea mayor que 7.

""" El resultado de la ejecución de este código es: {(2 , 4), (1, 2), 
(2, 1), (1, 5), (3, 1), (4 , 1), (1, 1), (5, 1),
(4, 2), (1, 4), (2 , 3), (3, 3), (2, 2), (3, 2), (1, 3)} """

""" import itertools
import math
def lazamientoDados(lista:list):
    contador= 0
    valor= itertools.product(lista,repeat=2)
    for i in valor:
        if sum(i)< 7:
            contador+=1
    return contador
print(lazamientoDados([1,2,3,4,5,6])) """


#escriba un codigo para enumerar los elementos del complemento 
lista=[]
rango= int(input("de 1 hasta que rango: "))
for i in range(1,rango):
    lista.append(i)   
multiplos3= set( filter(lambda x: x%3== 0,lista))
multiplos2= set(filter(lambda x: x%2==0 ,lista))
union= multiplos2.union(multiplos3)
print((multiplos3))
print((multiplos2))
print(union)
