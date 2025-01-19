import random

n= int(input("numero de participantes: "))
m= int(input("numero de rondas: "))
datos_rondas= []


for i in range(1,m+1):
    datos_ronda= []
    print(f"RONDA NUMERO {i}")
    ruleta= random.randint(1,5)
    for j in range(1,n+1):
        print("---------------------------------------------")
        
        valor= int(input(f"jugador {j} digite el numero a apostar en la ronda {i}: "))
        datos_rondas.append(ruleta)
        datos_ronda.append(valor)
        
    print(f"el numero que salio es: {ruleta}")
    print(f"los datos seleccionados en esta ronda fueron: {datos_ronda}")
    for x in range(len(datos_ronda)):
        if ruleta == datos_ronda[x]:
            print(f"el ganador fue el jugador {x+1}")
    x= 0   
conteo= {}    
for i in datos_rondas:
    conteo[i]= datos_rondas.count(i)
dato_menor= min(conteo,key=conteo.get)
veces_salio= conteo[dato_menor]
print(f"el dato que salio menos veces es {dato_menor}")