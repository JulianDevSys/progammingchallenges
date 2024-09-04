""" /*
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
 */ """
 
""" lista= [1,2,3,4,8,20,100]
arreglo_resultado= []   
tamaño= len(lista)
for i in range(tamaño-1):
    j=i+1
    if lista[i]>= lista[j]:
        raise "error"
    
    arreglo_resultado.append(lista[i])
    diferencia=lista[j]-lista[i]   
    if diferencia> 1:
        contador= lista[i]+1
        for k in range( contador, lista[j]):
            arreglo_resultado.append(k)    

print(arreglo_resultado) 

    
 """
 
#13////nformar si los dos arreglos son 
#iguales. Dos arreglos son iguales, si y solo si, posición a posición cada elemento de los dos arreglos es igua

""" arreglo1= [1,2,3,4,7,9,10,20,21,22]
arreglo2= [1,2,3,4,7,9,11,20,21,22]
for i in range(len(arreglo1)):
    if len(arreglo1) != len(arreglo2):
        print("los arreglos no son iguales")
    if arreglo1[i] == arreglo2[i]:
        bandera=True
    else:
        print(f"no son iguales por que arreglo1 en la posicion {i} tiene el numero {arreglo1[i]}")
        print(f"no son iguales por que arreglo2 en la posicion {i} tiene el numero {arreglo2[i]}")
        bandera=False
        break
if bandera== True:
    print("los arreglos son iguales")
     """
     
#14///////////////////buscar: un numero en el arreglo y decir e que posicion estaba/ empezando desde 1 y no 0
""" 
arreglo_numeros= [1,2,3,4,6,9,12,21,11,5,0]
valor_buscar= int(input("escriba el valor a buscar en el arreglo: "))
for i in range(len(arreglo_numeros)):
    if arreglo_numeros[i] == valor_buscar:
        print(f"el valor  {arreglo_numeros[i]} esta en la posicion: {i+1}")
    if valor_buscar not in arreglo_numeros:
        print(f"no esta el numero {valor_buscar} en el arreglo")
        break

 """
 
 #/////hacer un arreglo y obtener el valor menor y el mayor de este sin usar funciones propias del lenguaje
 
 
""" numeros= [12,2,15,4,4,5,7,9,2,0,13]
tamaño= len(numeros)
nuevo=0
for i in range(tamaño-1):
    
    if numeros[i]> numeros[i+1]:
        nuevo=numeros[i+1]
        numeros[i+1]=nuevo
       
    else :
        nuevo=numeros[i]
        numeros[i+1]=nuevo
print(nuevo)



#
numeros1= [2,12,0,5,7,9,13,1]
tamaño_arreglo= len(numeros1)
valor_minimo= 0
for i in range(tamaño_arreglo-1):
    j=i+1
    print(f"este {numeros[j]}")
    if numeros1[i]> numeros1[j]:
        valor_minimo=numeros1[j]
        numeros1[i]= valor_minimo 
        print(valor_minimo, numeros1[i])
    else:
        valor_minimo=numeros1[i]
        numeros1[j]= valor_minimo
        print("este")    
        print(valor_minimo, numeros1[i])
print(valor_minimo) """


#hacer producto punto con dos arreglos

""" a= [2,4,1]
b=[-4,6,-16]
ab= []
for i in range(len(a)):
    ab.append(a[i]* b[i])
total= 0
for i in ab:
    total+=i
print(total)  
     """
    
# invertir una lista
""" 
lista= [0,1,2,1,0,6,6,8,9]
arreglo2=[]
tamaño=len(lista)
for i in range(tamaño-1,-1,-1):
    print(i)
    arreglo2.append(lista[i])
print(arreglo2) """


#ejercicio  de FizzBuzz
""" Escribe una función que imprima los números del 1 al 100. Pero para múltiplos de tres, 
imprime "Fizz" en lugar del número, y para los múltiplos de cinco, imprime "Buzz".
Para números que son múltiplos de ambos tres y cinco, imprime "FizzBuzz". """

def FizzBuzz():
    for i in range(1,101):
        if i%3 == 0 and i%5==0:
            print("fizbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
FizzBuzz()
    
        

