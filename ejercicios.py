""" multiplicar= int(input("escriba la tabla que quiera: "))
for i in range(1,11):
    resultado= multiplicar * i
    print(f'{i}* 5 = {resultado}')     """
    
#////////////////////////////////////////////////////////////////

""" texto= input("escriba una frase: ")
contador= 0
for caracter in texto :
    contador+=1   
print(f"el numero total de caracteres es {contador}")
 """
 
 #////////////////////////////////////////////////////////////
""" lista_numeros= [1,2,3,4,5]
suma= 0
for i in lista_numeros:
    suma+= i
print(suma) """
#//////////////////////////////////////////////////////////////

""" lista_numeros= [1,2,3,4,5,8,6]
maximo = lista_numeros[0]
for i in lista_numeros:
    if i < maximo:
        maximo= i
print(maximo)    """
#///////////////////////invertir una cadena usando el bucle for///////////////////////////////////////

""" cadena_texto= input("dame una frase o palabra para invertir")
cadena_invertida= ""

for cadena in cadena_texto:
    cadena_invertida = cadena + cadena_invertida
    print(cadena_invertida)
print(f"asi queda : {cadena_invertida}")
 """
 
#////////////////////////////////////factorial usando bucle///////////////////////////////////////////////

""" factorial = int(input("digite un numero: "))
for i in range(1, factorial):
  factorial *= i
  print(factorial)
 """

#/// hacer un palindromo///////

def es_palindromo(palabra):
#    palabra = palabra.lower().replace(" ", "")
# metodo palabra[::-1] invierte la cadena
#funciona [inicio:fin:paso] al omitir las dos primeras y colocar -1 empieza de atras hacia adelante

        if palabra == palabra[::-1]:
            print(f'"{palabra}" es un palíndromo.')
        else:
            print(f'"{palabra}" no es un palíndromo.')
es_palindromo("anilina")
            
""" def verificar_palabras(cadena):
    palabras = cadena.split(" ")
    for palabra in palabras:
        if es_palindromo(palabra):
            print(f'"{palabra}" es un palíndromo.')
        else:
            print(f'"{palabra}" no es un palíndromo.') """

# Ejemplo de uso
#cadena = "Reconocer Ana radar nivel"
#verificar_palabras(cadena)
 
#///////////////////ejercicios////////////////

""" def verificar ():
    alumnos =[
        {'nombre': "julian",
        'edad': 19},
        {'nombre': 'esteban',
        'edad': 18},
        {'nombre': "roberto",
        'edad': 20},
        {'nombre': 'ricardo',
        'edad': 25}
    ]
#a diferencias de la lista de pasarle el valor 0 o 1 que es la posision,
#colocamos el valor que queremos comparar y traer
    alumnos.sort(key= lambda i:i['edad'])
    profesor= alumnos[-1]['nombre']
    asistente= alumnos[0]['nombre']
    return profesor, asistente
profesor,asistente= verificar()  
print(profesor, asistente)  
 """
""" 
#creamos la funcion compañeros
def obtener_compañeros(cantidad_compañeros):
#creamos la lista donde vamos a guardar todos los valores
    compañeros_Estudio=[]
#hacemos un bucle que funcione la cantidad de datos que diga el usuario
    for i in range(cantidad_compañeros):
        nombre= input("escriba su nombre: ")
        edad= int(input("escriba su edad: "))
#guarda en compañero el nombre y edad
        compañero=[nombre, edad]
#traemos la otra lista para guardar todos los valores que nos proporciono el usuario
        compañeros_Estudio.append(compañero)

#organizamos por orden(adentro va el parametro que hay que tener en cuenta para ordenarlo)
#se ustiliza el key= para decir que va a coger los valores del arreglo
# lambda indica una funcion anonima ( x es el parametro por ejemplo el valor que le colocamos a un bucle)
#es el nombre y decimos que x va a tomar el segundo elemendo
    compañeros_Estudio.sort(key=lambda x:x[1])
#el arreglo compañeros va a quedar en una lista de lista compañeros=[[julian,19], [esteban,20]]
#por lo cual para acceder a los valores serian asi
    asistente= compañeros_Estudio[0][0] # el primer numero nos dice el primer elemento, y el otro el nombre
    profesor=compañeros_Estudio[-1][0]
    return asistente,profesor
asis,prof= obtener_compañeros(3)
print(asis,prof)
 """


















