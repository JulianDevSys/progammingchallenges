""" #ejercicio 1
suma= 0
for i in range(11):
    suma+= i
print(suma)

#ejercicio 2
cantidad= int(input("escriba la cantidad de numeros a sumar: "))
suma= 0
for i in range(cantidad +1):
    suma += i
print(suma)
 """
 
""" #ejercicio 3
cantidadNumeros= int(input("cantidad de numeros que desee: "))
for i in range(1,cantidadNumeros + 1):
    if i % 2== 0:
        print(i) """
        

""" #ejercicio 4
numeros= int(input("cantidad: "))
contador= 0
contador1=0
for i in range(1,numeros + 1):
    if i%2== 0:
        contador +=1
    else:
        contador1+=1 
print(f"dantidad de pares: {contador}")
print(f"dantidad de impares: {contador1}") """


""" #ejercicio5

suma= 0
cantidad1= int(input("digite: "))
for i in range(cantidad1+ 1):
    suma+= i
print(suma) """


""" #ejercicio6
rango1=int(input("desde que numero desea empezar: "))
rango2= int(input("escriba hasta que numero: "))
for i in range(rango1, rango2+1):
    print(i) """
    

""" #ejercicio7
rango1=int(input("desde que numero desea empezar: "))
rango2= int(input("escriba hasta que numero: "))
suma= 0
for i in range(rango1, rango2+1):
   suma+=i
print(suma)
 """
 
"""  #ejercicio 8
 
for i in range(1,11):
    if i%2== 0:
       i=i*10
    print(i) """
    

#ejercicio 9

""" n= int(input("cantidad de datos: "))
i= 0
resultado= -1
while i < n:
    resultado *=-1
    print(resultado)
    i +=1 """
    
    
#primera forma de hacerlo
""" n= int(input("cantidad estudiantes: "))
contador4= 0
contador3= 0
contador2= 0
contador1= 0
contador= 0
for i in range(n):
    calificacion_estudiantes= input("escriba la calificacion: ")
    if calificacion_estudiantes.upper() == "A":
        contador += 1
    elif calificacion_estudiantes.upper()== "B":
        contador1+=1       
    elif calificacion_estudiantes.upper()== "C":
        contador2+=1
    elif calificacion_estudiantes.upper()== "D":
        contador3+= 1
    else:
        contador4 += 1
        
print(f"cantidad de A: {contador}")
print(f"cantidad de B: {contador1}")
print(f"cantidad de C: {contador2}")       
print(f"cantidad de D: {contador3}")
print(f"cantidad de F: {contador4}") """

#segunda forma de hacerlo
""" 
calificacion={
    'A': 0,
    'B': 0,
    'C':0,
    'D':0,
    'F':0,
}
cantidad_calificaciones=int(input("cantidad de notas a registrar: "))

for i in range(cantidad_calificaciones):
    calificacion_docente=input("escriba las calificaciones: ")
    if calificacion_docente.upper() in calificacion:
        calificacion[calificacion_docente]+=1
print(calificacion) 
     """






#//////////////////////Arreglos////////////////////////

#ejercicio 1
""" cantidad_enteros= int(input("cantidad de datos: "))
arreglo_numeros= []
for i in range(1,cantidad_enteros*2):
    if i%2==0:
        total= i*-1
    else:
        total=i
    arreglo_numeros.append(total)
print(arreglo_numeros) """

#ejercicio2

""" cantidad_enteros= int(input("cantidad de datos: "))
arreglo_numeros=[]
for i in range(2, cantidad_enteros*2, 2):
    if i%4== 0:
        resultado= i
    else:
        resultado= i*-1
    arreglo_numeros.append(resultado)
print(arreglo_numeros) """


#ejercicio3
""" arreglo=[]
cantidad_enteros= int(input("cantidad de datos: "))
for i in range(cantidad_enteros):
    if i%2==0:
        resultado= 1+(i//2)*4
        
    else:
        resultado= -(3+(i//2)*4)
    arreglo.append(resultado)
    
    
print(arreglo) """



#ejercicio 4
""" Llenar un arreglo de enteros de tamaño n, donde n es ingresado 
por el usuario con la siguiente serie numérica: 
1, 2, 4, 8, 16, 32, 64, 128, ….. hasta completar el tamaño el arreglo. """

#fue la primera solucion que se me ocurrio
""" ejercicio4= []
resultado= 1
datos1= int(input("escribe los datos: "))
for i in range(datos1):
    if i==0:
        resultado= 1
    else:
        resultado*=2  
    ejercicio4.append(resultado)
print(ejercicio4) """