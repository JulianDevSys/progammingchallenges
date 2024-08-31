
#funciones simples

""" def saludar():
    print("hola muchachos")
saludar() """
#//////////////// tablas
""" def tablas (tabla):
    for i in range(1, 11):
        multiplicar= tabla * i
        print( multiplicar)
        
tablas(5) """
#//////////////////
""" def saludar2(nombre, sexo):
    if sexo== 'f':
        print(f'bienvenida señorita {nombre}')
    elif sexo == 'm':
        print(f'bienvenido señor {nombre}')
saludar2('julian', 'm') """

#usando lambda

saludando= lambda nombre,sexo : print(f"bienvenida{nombre}") if sexo=="f" else print(f"bienvenido  {nombre}") if sexo=="m" else None
saludando("julian", "m")
#/////////////////////contraseña aleatoria////////////////////

""" #creamos la funcion para hacer la contraseña
def contraseña_aleatoria(numero):
#la cadena de texto que vamos a recorrer para hacer la contreaseña
    cadena_texto= 'abcd3fghij'
#converimos el numero dato en string para poder recorrerlo
    converti_string = str(numero)
#despues convertimos a entero el primer digto
    converti_entero= int(converti_string[0])
 #primer digito va a tomar estos valores   
    c1= converti_entero - 2
    c2=converti_entero
    c3= converti_entero - 5
#el resultado va a ser la cadena texto en esas posiciones  
    resultado = f"{cadena_texto[c1]}{cadena_texto[c2]}{cadena_texto[c3]}{converti_entero*2}"
    return resultado

result= contraseña_aleatoria(754)
print(result) """
    

 #///// funciones anonimas--lambda vs funciones normales////////////////
 
numeros= [1,2,3,4,5,6,7,8,9,10]
#creando la funcion
def num_pares(num):
    if num%2== 0:
        return True
#usando filter con una funcion
# primer dato que resive es la funcion, segundo datos los parametros( en este caso la lista)
numerosPares= filter(num_pares,numeros)
#tenemos que convertirlo a lista para que nos de los valores
#filter funciona como un bucle
print(list(numerosPares))

#sefunda forma de hacerlo con lambda
#cogemos la variable donde vamos a guardar, usamos lambda, le damos la condicion, y segundo parametro(los datos)
num_par= filter(lambda numero:numero%2==0, numeros)
#al usar filter lo convertimos en lista
print(list(num_par))






