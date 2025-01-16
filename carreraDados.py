import random

jugadores= [0,0]
suma= 0

j=1
while jugadores[0] < 50 and jugadores[1] < 50:
    i= 0
    print(f"lanzamiento numero {j}")
    while i < 2:
        dado1= random.randint(1,6)
        dado2= random.randint(1,6)
        if dado1== dado2:
            print(f"salieron los dados iguales, para el jugador{i+1} :{dado1}, {dado2}")
            print(f"el jugador{i+1} empieza la carrera")
            suma= dado1+dado2
            jugadores[i]+= suma
            print(f"jugador {i+1} lleva {jugadores[i]}")
        else:
            print(f"no salieron los dados iguales, {dado1}, {dado2}")
        i+=1
    j+=1
print(f"resultados jugador1: {jugadores[0]} y jugador2: {jugadores[1]}")  
if jugadores[0] == 50:
    print(f"felicidades el jugador 1 gano la carrera con {jugadores[0]}")
else:
    print(f"felicidades el jugador 2 gano la carrera con {jugadores[1]}")
    
