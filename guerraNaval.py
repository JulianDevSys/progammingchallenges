#ejercicio guerra naval
""" Implementa un juego básico de Guerra Naval donde el jugador tenga que hundir barcos en un tablero de 10x10. 
Los barcos pueden ser de diferentes tamaños (por ejemplo, 2x1, 3x1, etc.). El juego debe permitir al jugador hacer disparos y mostrar el resultado después de cada tiro. 
Puedes usar listas para representar el tablero y colocar los barcos aleatoriamente.

 """
import random


arreglo=[]

for i in range(1,5):
    x= random.randint(-5,5)
    y=random.randint(1,10)
    arreglo.append((x,y))
    

arreglo1=[]
for i in range(1,5):
  JugadorX= int(input("digite la posicion en x del barco : "))     
  Jugadory= int(input("digite la posicion en Y del barco : ")) 
  arreglo1.append((JugadorX,Jugadory))
  
print(arreglo)  
while len(arreglo1)>0 and len(arreglo)>0:
    disparoMaquina=((random.randint(-5,5),random.randint(-10,-1)))
    if disparoMaquina in arreglo1:
        arreglo1.pop(arreglo1.index(disparoMaquina))
        print("barco golpeado")
    else:
        print("objetivo fallado")
    
    disparoJugadorX=int(input("posicion en x que deseas disparar: "))
    disparoJugadorY=int(input("posicion en y que deseas disparar: "))
    if (disparoJugadorX,disparoJugadorY) in arreglo :
        arreglo.pop(arreglo.index((disparoJugadorX,disparoJugadorY)))
        print("barco golpeado")
    else:
        print("objetivo fallado")

print("gano la maqiona") if len(arreglo1)==0 else print("gano el jugador")
    
    


