# funcion cuadrado
#aprendiendo a usar map
""" lista= [1,2,3,4,5,6]
valor= map(lambda x: x*x,lista)
print(list(valor)) """
#primera practica
""" lista2= ["1",4,5,"6",8,9]
resultado= map(str,lista2)
print(list(resultado)) """
#segunda practica
""" lista3= [1,3,9,2]
lista4= [1,3,4,5]
suma=map(lambda x,y: x+y,lista3,lista4)
print(list(suma)) 
 """
#Obtener la longitud de cada palabra
""" palabras = ["map", "python", "funcion", "programacion"]
longitud_cadena=map(lambda x: len(x),palabras)
print(list(longitud_cadena))
 """
 
#Convertir temperaturas de Celsius a Fahrenheit( formula es celsius * 9/5 + 32)
""" celsius = [0, 20, 37, 100]
Fahrenheit= map(lambda x: x * 9/5 +32,celsius)
print(list(Fahrenheit)) """

# Filtrar y transformar en una sola línea
""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrar_pares= map(lambda x: x*x,filter(lambda x: x%2!=0, numeros))
print(list(filtrar_pares)) """

#Unir elementos de dos listas en tuplas
""" nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30, 35]
unir_listas= map(lambda x,y:(x,y), nombres,edades)
print(list(unir_listas)) """

#Modificar diccionarios en una lista
#Dada una lista de diccionarios donde cada diccionario representa a una persona, utiliza map() 
# para agregar una nueva clave full_name que sea la combinación de first_name y last_name.


# items se utuliza en diccionarios..... no en lista de diccionarios ya que este tra cla vealor
""" personas = [
    {"first_name": "John", "last_name": "Doe"},
    {"first_name": "Jane", "last_name": "Smith"},
    {"first_name": "Emily", "last_name": "Jones"}
]


def funcion (persona):
    full_name= persona["first_name"]+ " " + persona["last_name"]
    persona["full_name"]= full_name
    return persona
nuevo_diccionario= map(funcion,personas)
print(list(nuevo_diccionario)) 
 """



#sacar descuento con map en el diccionario
""" precios = {'manzana': 100, 'naranja': 80, 'banana': 50}

#no se le podria pasar el .items() por que lambda recibe un numero no una tupla
descuento=map(lambda x: (x[0], x[1]- float(x[1]* 0.10)), precios.items())

print(list(descuento)) """

#sacar descuento(practicando)
""" precios_consola = {'play': 200, 'xbox': 130, 'celular': 90}

iva= map(lambda valor_iva: (valor_iva[0], valor_iva[1] + valor_iva[1]*0.15) ,precios_consola.items())
print(dict(iva)) """



#////////////////////////////////
""" lista_familia= [
    {"nombre":"alba lucia", "apellido": "henao"},
      { "nombre": "Helmer", "apellido": "castro"},
        { "nombre": "luis Muguel", "apellido": "castro"
     }
    ] """
#primera forma de hacerlo
""" nuevo1=map(lambda x: {**x, "nombre_completo" :x["nombre"]+ " "+ x["apellido"]}, lista_familia)
print(list(nuevo1))
 """
#segunda forma de hacerlo
""" 
def juntar_nombre(p):
  nombre_completo=   p["nombre"] + " " +p["apellido"]
  p["nombre_completo"]= nombre_completo
  return p

nuevo= map(juntar_nombre, lista_familia)
print(list(nuevo)) """


#////////////////////
#con ** podemos sobreescrbir un diccionario
#** podemos agregar cosas al diccionario
mi_diccionario = {
    "nombre": "Juan",
    "apellido": "roberto",
    "edad": 30,
    "ciudad": "Madrid"
}

agregar_datos={**mi_diccionario, "nombre" : "julian", "edad": 20, "ciudad": "tulua"}
print(agregar_datos)

full_name_persona=lambda x: {**x, "nombre_completo": x["nombre"] +" " + x["apellido"]}
diccionario= full_name_persona(mi_diccionario)
print(diccionario)

