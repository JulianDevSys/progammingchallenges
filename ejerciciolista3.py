#Rotación de una lista()-->Escribe un programa que rote una un numero de la lista a la derecha o a la izquierda un número específico de veces.

""" numero_rotar= int(input("escribe el numero que quieres cambiar la posicion: "))
lista =[1,2,4,6,7,9,10,15]
tamaño=len(lista)-1
total= 0
for i in range(tamaño):
    if numero_rotar== lista[i]:
        numero_posiciones= int(input("cuantas posiciones desea moverlo: "))
        direccion_rotacion= input("a que direccion desea moverlo D o I: ")
        if direccion_rotacion.upper()== "D":
            guardar=i+1
            i+=numero_posiciones
            if i > tamaño:
                total= i-tamaño
                i= total-1
                lista.insert(i,numero_rotar)
                lista.pop(guardar)
                break
        else:
            direccion_rotacion.upper()=="I"
            guardar=i
            i-=numero_posiciones
            if i < 0:
                print(i)
                lista.pop(guardar)
                lista.insert(i,numero_rotar)
                
                break
               
  
        
print(lista) """



def buscar_elemento_lista(buscar_numero,lista,numero_posiciones_mover,direccion_rotacion):
    if buscar_numero not in lista:
        print( f"el elemento {buscar_numero} no se encuentra en la lista")
        return lista
#nos va a decir el indice donde se encuentra el numero
    ubicacion_elemento=lista.index(buscar_numero)
    
    if direccion_rotacion.upper()== "D":
        nueva_posicion= (ubicacion_elemento + numero_posiciones_mover)% len(lista)
    elif direccion_rotacion.upper()=="I":
        nueva_posicion= (ubicacion_elemento- numero_posiciones_mover)% len(lista)
    else:
        print("solo esta la posicion I y D ")
        return lista
        
    lista.pop(ubicacion_elemento)
    lista.insert(nueva_posicion,buscar_numero)
    return lista

lista = [1, 2, 4, 6, 7, 9, 10, 15]
buscar_numero = int(input("Escribe el número que quieres cambiar la posición: "))
if buscar_numero in lista:
    numero_posiciones_mover = int(input("¿Cuántas posiciones deseas moverlo?: "))
    direccion_rotacion = input("¿A qué dirección deseas moverlo? (D o I): ")
    lista_resultado = buscar_elemento_lista(buscar_numero, lista, numero_posiciones_mover, direccion_rotacion)
    print("Lista resultante:", lista_resultado)
else:
    print(f"El número {buscar_numero} no está en la lista.")
#/////////////////////////////////////////////
