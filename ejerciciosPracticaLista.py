""" familia=["esteban", "julian", "sergio", "luis", "papa", "mama", "mama", "esteban", "sergio"]

diccionario_familia= dict()

for i in familia:
    if i not in diccionario_familia:
        diccionario_familia[i]=True
print(diccionario_familia)
 """

#Dado un diccionario, crea un nuevo diccionario donde las claves y los valores estén invertidos.

""" diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario_nuevo= {}

for i in diccionario:
    if i not in diccionario_nuevo:
        diccionario_nuevo[diccionario[i]]=i
    
print(diccionario_nuevo) """

#Dada una lista de palabras, agrúpalas en un diccionario donde la clave sea la longitud de la palabra y el valor sea una lista de palabras con esa longitud.
""" palabras = ['cat', 'dog', 'elephant', 'mouse', 'rat']
cantidad_palabras= dict()
for i in palabras:
    if len(i) not in cantidad_palabras:
        cantidad_palabras[len(i)]=[i]
    else:
        cantidad_palabras[len(i)].append(i)
        
print(cantidad_palabras) """

#////////////////////////
    
# Dada una frase (cadena de texto), crea un diccionario que cuente cuántas veces aparece cada letra (ignorando espacios y mayúsculas).

""" frase= input("escriba la frase: ")
contador_letras= dict()
for i in frase.upper():
    if i == " ":
        continue
    if i not in contador_letras:
        contador_letras[i]= 1
    else:
        contador_letras[i]+=1
       
print(contador_letras) 
     """


#Dado un diccionario, ordena las claves por sus valores en orden descendente y muestra el diccionario ordenado.

diccionario = {'a': 3, 'b': 1, 'c': 2}





#Dado un diccionario con valores numéricos, elimina los pares clave-valor con el valor mínimo





















