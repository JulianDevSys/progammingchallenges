""" 
def buscar_elemento(lista:list, elemento):
    for i in lista:
        if elemento== i:
            return f"el {elemento} fue encontrado en la posicion {lista[i-1]}"
        if i == len(lista):
            return "el elemento no se encuentra en el arreglo"
        else:
            continue
print(buscar_elemento([1,2,3,6,9,4,7],6)) """




#ejercicio hormiga forma 1
import random
import math
def mover_hormiga(n):
    lista= ["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA" ]
    limite= [10,-10]
    hormiga=[-2, 2]
    arroz= [10 ,8]
    contador=0
#vamo a calcular la distancia maxima con la formula general
    distancia_maxima_hormiga=0
#usamos esto para saber la o¿posicion actual de la hormga
    posicion_mas_lejana= hormiga[:]
    for i in range(n):

        valor= random.choice(lista)
        movimiento_aleatorio=random.randint(1,3)
        contador+=movimiento_aleatorio
           
        if valor== "ARRIBA":     
            hormiga[1]+=movimiento_aleatorio
            if hormiga[1] > limite[0]:
                hormiga[1]-= movimiento_aleatorio*2
        elif valor== "ABAJO":
            hormiga[1]-=movimiento_aleatorio
            if hormiga[1] < limite[1]:
                hormiga[1]+= movimiento_aleatorio*2
        elif valor== "IZQUIERDA":
            hormiga[0]-=movimiento_aleatorio
            if hormiga[0] < limite[1]:
                hormiga[0]+= movimiento_aleatorio*2
        elif valor== "DERECHA":
            hormiga[0]+=movimiento_aleatorio
            if hormiga[0] > limite[0]:
                hormiga[0]-= movimiento_aleatorio*2
        #print(i," ",hormiga)
        if hormiga== arroz:
            print(f"encontro el arroz  en {contador} pasos")
            break          
        distancia_actual= math.sqrt((arroz[0]- hormiga[0])**2 +(arroz[1]-hormiga[1])**2)
        if distancia_actual > distancia_maxima_hormiga:
            distancia_maxima_hormiga=distancia_actual
            posicion_mas_lejana=hormiga[:]
        
    if hormiga != arroz:
        print (f"la hormiga quedo en {hormiga} y no pudo encontrar el arroz que esta en la posicion {arroz}")
    return f"esta es la distancia mas lejan en la que se encontro la hormiga {distancia_maxima_hormiga } en la posicion {posicion_mas_lejana}"



#ejercicio hormiga forma mas optima
from random import randint,choice
def simulation():
    limits = [100,100] #x , y
    init_coordenates_rice = [randint(-limits[0],limits[0]),randint(-limits[1],limits[1])]# x , y
    coordenate_ant = [randint(-limits[0],limits[0]),randint(-limits[1],limits[1])]# x , y
    max_distance = float('-inf')
    k = 0
    
    for i in range(100):  
        steps = randint(1,3)     
        coordenate = randint(0,1)      
        sentido = choice([-1,1])      
        a = coordenate_ant[coordenate]+ steps*sentido    
        if   abs(a) <= limits[coordenate]:
            coordenate_ant[coordenate]+= steps*sentido
        else:
            coordenate_ant[coordenate]+= steps*sentido*-1    
        d=  math.sqrt(math.pow(init_coordenates_rice[0]-coordenate_ant[0],2)+math.pow(init_coordenates_rice[1]-coordenate_ant[1],2))       
        if (d>max_distance):
            max_distance = d          
        k+=1
        
        if(coordenate_ant == init_coordenates_rice):
            return (True,max_distance,k,init_coordenates_rice,coordenate_ant)   

    return (False,max_distance,k) 

for j in range(1000):
    print(mover_hormiga(100)) 
    
    
    
    
    
    
    
    
    
