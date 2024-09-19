#enunciado ejercicio tiro al blanco
""" es un juego que consiste en lanzar dardos a un objetivo circular.
El premio que gana el jugador, depende de la ubicación en la
cual cae el dardo y su valor se reparte en dólares ($30, $40 o
$50) """

""" Existen 3 círculos concéntricos (que tienen el mismo centro) y las longitudes de los radios del primero, segundo y tercer
círculos son 10cm, 40cm y 80cm, respectivamente.Suponga que los 3 círculos están inscritos en un cuadrado de longitud de lado 160cm.

Escriba un algoritmo que permita simular n lanzamientos aleatorios de dardos, asignando
de forma aleatoria pares ordenados (x, y) en el cuadrado descrito.
En cada lanzamiento se debe verificar si el dardo se ubica al interior de alguno de los
círculos descritos y asignar el respectivo premio.
Al final, muestre el premio total en dólares que obtuvo el jugador. """

import random
import math
import matplotlib.pyplot as plt

def tiro_blanco(numero_lanzamientos):
    dardos_x = []
    dardos_y = []
    premios = []
    premio= 0
    for i in range(1, numero_lanzamientos+1):
        lanzamientos_x= random.uniform(-80,80)
        lanzamientos_y =random.uniform(-80,80)
        #agregamos cada lanzamiento a una lista para graficarlo despues
        dardos_x.append(lanzamientos_x)
        dardos_y.append(lanzamientos_y)
        
        posicionDardo= math.sqrt(lanzamientos_x**2 + lanzamientos_y**2)
        print(f"el lanzamiento numero: {i} dio en el {posicionDardo}")
        if(posicionDardo <10):
            premio+=50
        elif(posicionDardo >= 10 and posicionDardo <40 ):
            premio+=40
        elif(posicionDardo>=40 and posicionDardo <80):
            premio+= 30

        
        premios.append(premio)
       
    #1--numero indica la cantidad graficos en filas por si se va a graficar mas de una cosa
    #2---> el segundo numero indica la cantidad graficos en columnas por si va a colocar uno al lado
    #3--siempre dejelo 1  xd
    plt.subplot(1, 1, 1)
    
    #cogemos los areglos de los valores en "x" y  "y", c= color que va coger ese punto, opacidad de los puntos(colocar ese siempre)
    plt.scatter(dardos_x, dardos_y, c='blue', alpha=0.5, label='Dardos lanzados')
    plt.title('Distribución de Dardos')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    #las linas del medio  en y y x del plano cartesiano 
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Añadir círculos para visualizar las zonas de premio
    #(0,0) inidica que los circulos se encuentran centrados, deespues el color de cada circulo el estilo y la opacidad
    circle1 = plt.Circle((0, 0), 10, color='green', fill=False, linestyle='--', linewidth=1, label='10 cm (50 dólares)')
    circle2 = plt.Circle((0, 0), 40, color='yellow', fill=False, linestyle='--', linewidth=1, label='40 cm (40 dólares)')
    circle3 = plt.Circle((0, 0), 80, color='red', fill=False, linestyle='--', linewidth=1, label='80 cm (30 dólares)')
    
    #grafica cada uno de los circulo
    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(circle3)
    
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.xlim(-90, 90)
    plt.ylim(-90, 90)

  
    # Mostrar los gráficos
    plt.tight_layout()
    plt.show()

        
        
    return f"el premio fue: {premio} dolares"
print(tiro_blanco(5))

