#Normalización de Datos
personas = [
    {"nombre": "JOHN DOE", "telefono": "(123) 456-7890"},
    {"nombre": "JANE SMITH", "telefono": "1234567890"},
    {"nombre": "ALICE JOHNSON", "telefono": "123.456.7890"}
]

#puntos claves 
# isdigit()---> nos detecta si el valor es numero y no lo llama en caso de que no lo ignora
#enumerate--> coge el digito en vez del indice i= indice  lista[i] valor eso hace el enumerate
""" 
def normalizar_datos(x):
    nombre_minuscula=x["nombre"].lower()
    nuevo_valor= ""
    for i in x["telefono"]:
        if i.isdigit():
            nuevo_valor+=i
    diccionario_normalizado= ""
    for i , digito in enumerate(nuevo_valor):
        if i > 8:
            diccionario_normalizado+=digito
            break
        if i > 0 and i%3==0:
            diccionario_normalizado+= "-"
        diccionario_normalizado+=digito
        
    return {"nombre": nombre_minuscula,
            "telefono": diccionario_normalizado}
    
resultado= map(normalizar_datos,personas)
print(list(resultado))
    
 """


#Extracción de Datos de Archivos JSON
""" Tienes una lista de archivos JSON que contienen datos de productos. Cada archivo JSON es una cadena 
y contiene un campo precio que es un string con símbolos de moneda 
y separadores de miles. Necesitas extraer el precio y convertirlo a un número flotante. """



#datos en tener en cuenta:
#se debe importar la libreria json
#se debe usar la funcion json.loads() para pasarlo a diccionario
""" import json

archivos_json = [
    '{"producto": "Laptop", "precio": "$1,299.99"}',
    '{"producto": "Smartphone", "precio": "$799.00"}',
    '{"producto": "Tablet", "precio": "$349.50"}'
]


def extraccion_json(j):
    data=json.loads(j)
    nueva_cadena= ""
    for i in  data["precio"]:
        if i is "$":
            i.replace("$", "")
            continue
        if i is ",":
            i.replace(",","")
        
        else:
            nueva_cadena+= i

      
    return{
        "producto": data["producto"],
        "precio":float(nueva_cadena)
    }
Resultado= map(extraccion_json,archivos_json)
print(list(Resultado)) """


#Cálculo de Longitudes de Cadenas
#el objetivo es calcular la longitud de cada frase en una lista de frases y devolver esos valores en una lista de enteros
""" frases = [
    "Hola mundo",
    "Python es divertido",
    "¡Vamos a programar!",
    "Ejercicio completado"
]

longitud_frase= map(lambda x: len(x), frases)
print(list(longitud_frase)) """


#Filtrado y Transformación de Datos
""" empleados = [
    {"nombre": "Carlos", "salario": 48000},
    {"nombre": "Marta", "salario": 60000},
    {"nombre": "Luis", "salario": 52000},
    {"nombre": "Ana", "salario": 47000}
]
# no se itera por que son valores numericos
def incremento_salario(s):
    salarios= 0
    valor=0
    if s["salario"] >= 50000:
        salarios=  s["salario"]+ s["salario"]*0.10
        valor=salarios
    else:
        valor= s["salario"] 
    return{
        "nombre":s["nombre"],
        "salario": float(valor)
    }
    
resultado= map(incremento_salario,empleados)
print(list(resultado))
         """


















