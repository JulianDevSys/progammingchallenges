import random


def hundir_barco():
    n= int(input("numero municiones: "))
    barco_enemigo= [1,5]
    cañon= [3,8]
    direcciones= ["N", "S", "E", "O"]
    hundidos= 0
    for i in range(1,n+1):
        print(barco_enemigo)
        print(f"intento numero {i} ")
        print("----------------------------------------------------------------------------------")
        disparo_x= int(input("cordenadas en x donde quieres disparar: "))
        disparo_y= int(input("cordenadas en y donde quieras disparar: "))
        
        direccion_desplazamiento= random.choice(direcciones)
        movimiento_barco= random.randint(1,3)
        
        if direccion_desplazamiento== "N":
            barco_enemigo[1]+= movimiento_barco
        
        elif direccion_desplazamiento== "S":
            barco_enemigo[1]-=movimiento_barco
            
        elif direccion_desplazamiento== "E":
            barco_enemigo[0]+= movimiento_barco
            
        else:
            barco_enemigo[0]-=movimiento_barco
            
        print(f"disparos: {n-i}")
        print(f"hundido: {hundidos}")
        if disparo_x== barco_enemigo[0] and disparo_y==barco_enemigo[1]:
            print( f"hemos hundido el barco con tan solo {i} intentos")
            hundidos+=1
        
        else:
            print("estivimos cerca mi capitan....... en la sigueiente lo lograremos")
            if i==n:
                print(f"la nueva ubicacion del barco enemigo es:  {barco_enemigo} se movio al {direccion_desplazamiento}, casillas: {movimiento_barco} ")
                return("no mis camaradas, nos quedamos sin municiones, hemos perdido el combate, se nos escapo")
        
        print(f"la nueva ubicacion del barco enemigo es:  {barco_enemigo} se movio al {direccion_desplazamiento}, casillas: {movimiento_barco} ")


print(hundir_barco())