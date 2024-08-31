""" 
textoMayuscula= "hola mundo"
print(textoMayuscula.upper()) """

#metodos lista

""" frutas = ['manzana','platano','cereza','naranja']

for i in range(len(frutas)):
    if i == 0:
        print(frutas[i])
    elif i== len(frutas)-1:
        print(frutas[i])
        
        
frutas.pop(2)
frutas.insert(2, 'kiwi')

print(frutas)

numeros= [1,2,3,4,5]
suma= 0
for numero in numeros:
#for i in range(len(numeros)+1):
    suma +=i
print(suma) """


familia=  {'nombre': "julian",
     'apellido': "castro",
     'edad': 19}
"""     
    {'nombre': "esteban",
     'apellido': "castro",
     'edad': 19},   
    
    {'nombre': "lucia",
     'apellido': "henao",
     'edad': 35},     
   ] """

""" print(familia[0]) """

""" clave= familia.keys()
valor= familia.get('edad')
print(clave)
print(valor) """


""" numero = int(input("dame un numero: "))
multiplicar = numero * 3

print(multiplicar) """


#ejercicio1 

""" texto = input( "decime cualquier cosa: ")
separarPalabras= texto.split(" ")
print(separarPalabras)
cantidad= len(separarPalabras)
print(cantidad)
palabras = 2
cantidadPalabras= cantidad/ palabras

print(f"el tiempo que se demoro fue de:  {cantidadPalabras} segundos") """


#teoria de conjuntos

conjunto1 = {1,3,5, 7}
conjunto2 = {1,3,7}
# conjunto 2 es subconjunto del conjunto 1
#otra forma es colocar conjunto2 <= conjunto1 ( lo mismo pregunta si es subconjunto)
resultado = conjunto2.issubset(conjunto1)
#pregunta si es superconjunto 
#otra forma es decirle si conjunto2 > conjunto1 
resultado1= conjunto2.issuperset(conjunto1)
#verificar si algun numero en comun 
resultado2= conjunto2.isdisjoint(conjunto1)
print(resultado)
print(resultado1)
print(resultado2)