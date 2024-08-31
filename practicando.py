""" 

diccionario_familia= [
    {'nombre': 'julian', 'edad':19},
    {'nombre': 'esteban', 'edad':19},
    {'nombre': 'luis Miguel', 'edad':29},
    {'nombre': 'Sergio Andres', 'edad':28},
    {'nombre': 'Helmer', 'edad':56},
    {'nombre': 'Alba Lucia', 'edad':54},    
]

diccionario_familia.sort(key=lambda x:x['edad'])
mayor= diccionario_familia[-1]['nombre']
menor= diccionario_familia[0]['nombre'] 

print(mayor, menor)



def practicando_lista(cantidad):
    listaFamilia_completa= []
    for i in range(cantidad):
        nombre= input("escriba su nombre: ")
        sueldo= float(input("escriba su sueldo: "))
        familia= [nombre, sueldo]
        listaFamilia_completa.append(familia)
        listaFamilia_completa.sort(key= lambda x: x[1])
    mayor_sueldo = listaFamilia_completa[-1][0]
    return mayor_sueldo
mayorSueldo = practicando_lista(3)
print(mayorSueldo) """


#funcion que me de los numeros pares
def numeros_pares(numero):
    total_datos= []
    for i in range(1, numero+1):
        if i%2==1:
            continue
        else :
            lista_numeros= (i)
            total_datos.append(lista_numeros)
    return total_datos
total= numeros_pares(15)
print(total)



#/////////calculadora DE edad////////

def Calculadora_edad():
    i= True
    while i :
        año_nacimiento= int(input("escriba su año de nacimiento: "))
        año_actual= 2024
        if año_nacimiento > año_actual:
            print( "no has nacido")
        else:
            edad_total= año_actual- año_nacimiento
            return edad_total
edadUsauario= Calculadora_edad()
print(edadUsauario) 

#////////// contador de palabras/////////

def Contador_palabras():
    contador= 0
    frase= input("escriba una frase: ")
    palabra= frase.split(" ")
    for i in enumerate(palabra ):
        contador+= 1
    print(contador)
Contador_palabras() 




diccionario= [
    {'nombre': 'julian',  'ocupacion': 'estudiante', 'edad': 19},
    {'nombre': 'esteban',  'ocupacion': 'estudiante', 'edad': 19},
    {'nombre': 'roberto',  'ocupacion': 'trabaja', 'edad': 21},
]
#el diccionario.sort (la llave = FUNCION parametro: condicion(parametro[edad]))
diccionario.sort(key= lambda x:x['edad'])
mayor= diccionario[-1]['nombre']

print(mayor)