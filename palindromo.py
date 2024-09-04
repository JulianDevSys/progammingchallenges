#/// verificar si es un palindromo///////

def es_palindromo(palabra):
    palabra.upper()
    if palabra== palabra[::-1]:
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')

#///////////////////////////////verificar una cadena si es palindromo usando la funcion es_palindromo////////////////////////
def verificar_palabras(cadena):
    palabras = cadena.split(" ")
    for palabra in palabras:
        es_palindromo(palabra.upper())
cadena = "Reconocer Ana radar nivel"
verificar_palabras(cadena)



#verificar si una palabra es palindromo con recursividad

def palindromo(palabra):
    if len(palabra)<= 1:
        return True   
    elif palabra[0]== palabra[-1]:
        return palindromo(palabra[1:-1])    
    else:
        return False       
print(palindromo("rapar"))  


   
#determinar si unalista de numeros es palindrome
def lista_palindromo(lista:list):
    palindrome= []
    tamaño=len(lista)
    for i in range(tamaño-1,-1,-1):
        palindrome.append(lista[i])
    for i in range(tamaño):
        if lista[i]== palindrome[i]:
            bandera= True
        else:
            bandera=False
    if bandera==True:
        return("el arreglo es un palindrome")
    else:
        return("el arreglo no es un palindrome") 
print(lista_palindromo([0,1,2,1,0]))