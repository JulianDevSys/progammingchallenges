# hacer factorial
""" def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n* factorial(n-1)
        
print(factorial(5)) """

#/// potencia
""" def potencia(n,l):
    if l == 0:
        return 1
    else:
        return n* potencia(n,l-1)   
print(potencia(2,3)) """

#////////////////
""" def fibonacci(n):
    if n== 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2) 
print(fibonacci(10)) """
    
#crear un funcion que tome un numero positivo como argumento e imprima los numeros desde dicho argumento hasta cero

""" def contador_numeros(numero,lista=None):
    if lista== None:
        lista=[]
    if numero<0:
        return lista
    else:
        lista.append(numero)
        return contador_numeros(numero-1,lista)

print(contador_numeros(10)) """


#Calcula la suma de los primeros n números naturales (1 + 2 + 3 + ... + n).

""" def suma_numeros(n):
    if n < 1:
        return n
    else:
        return n+ suma_numeros(n-1)
print(suma_numeros(5)) """

#Cuenta el número de dígitos en un número positivo n.
""" 
def contar_digitos(numero):
    if numero < 10:
        return 1 
    else:
        return 1+ contar_digitos(numero//10)
    
    
print(contar_digitos(23458)) """

    


    
#///////// invertir una cadena con recursividad

""" def invertir(palabra):
    if len(palabra)==0:
        return palabra
    
    else:
        return invertir(palabra[1:])+palabra[0] 
    
print(invertir("castro")) """
         

#Escribe una función recursiva para calcular la potencia de un número.
# La función debería tomar como entrada una base a y un exponente b y devolver a^b.
      
""" def potencia(a,b):
    if b <= 1:
        return a   
    else:
        return a *(potencia(a, b-1))
       
print(potencia(3,3)) """

#Escribe una función recursiva que encuentre el valor máximo en una lista de números.

""" def max_elmento(lista:list):
    if len(lista) == 1:
        return lista[0]
    
    elif lista[0]< max_elmento(lista[1:]):
        lista[0]= max_elmento(lista[1:])
        return lista[0]
        
    else:
        return lista[0] 
          
print(max_elmento([2,20,1,21,8,3,15,22,0,5]))
 """

#Implementa una función recursiva que sume todos los elementos de una lista.

""" def sum_elementos(lista:list):
    if len(lista)==1:
        return lista[0]
    
    else:
        return lista[0] + sum_elementos(lista[1:])
        
print(sum_elementos([1,2,3,4,5,6,7,8,9,10]))
 """
    
#Escribe una función recursiva que busque un elemento en una lista
# y devuelva True si el elemento está presente y False en caso contrario.

""" def buscador_numeros(numero, lista:list):
    if len(lista)== 0:
        return False
    
    if numero != lista[0]:
        return  buscador_numeros(numero,lista[1:])

    else:
        return True         
print(buscador_numeros(5,[1,2,3,4,5,6,7,8,9,10,15])) """
    


#cuenta regresiva que aparezca cada numero
""" def cuenta_regresiva(n):
    if n < 1:
        print(n)
    else:
        print(n)
        cuenta_regresiva(n-1)        
cuenta_regresiva(5) """
        


#Suma de dígitos
#Escribe una función recursiva que tome un número entero positivo y devuelva la suma de sus dígitos.

""" def suma_digitos(n): 
    convertir=str(n)
    if len(convertir)== 1:
        return int(convertir)
    else:
        return int(convertir[0]) + suma_digitos(int(convertir[1:]))
        
print(suma_digitos(5)) """  
""" 

numero = "123"
print(int(numero[0]) + int(numero[1]))
 """
# hacer anagrama

""" def anagrama(word1, word2,i):
    print(word1,word2,i)
    if(len(word1)!= len(word2)):
        return False

    if(not word1[i] in word2  or not word2[i] in word1):
        return False

    if   word1.count(word1[i]) != word2.count(word1[i]) or word2.count(word2[i]) != word1.count(word2[i]):
        return False

    if(i == len(word1)-1):
        return True
    
    return True and  anagrama(word1,word2,i+1)

print(anagrama("rata","tara",0))
print(anagrama("ratta","tarra",0)) """

# crear una funcion que sume todos los elementos de un arreglo meudnate recursividad

""" def suma_arreglo(lista:list):
    if len(lista)== 1:
        return lista[0]
    else:
        return lista[0] + suma_arreglo(lista[1:])
                
print(suma_arreglo([1,2,3,4,5,6,7,8,9,10]))
 """

#Hacer una funcion que reciba un numero y lo convierta a bianario 


""" def toBinario(numero):#
    if numero== 0:
       return "0" 
    if numero== 1:
       return "1" 
   
    if numero % 2== 0:
       return   toBinario(numero/2) +"0"
    else:
       return  toBinario(int(numero/2)) + "1"
       
lista1 =  ["1","3",3,"0",1,1,2,2]  

x= list(map(lambda x: toBinario(int(x)), lista1))
print(x)
 """
 
 




    