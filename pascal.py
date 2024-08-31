""" /*
 * Crea un programa que sea capaz de generar e imprimir todas las
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 */ """
import itertools
palabra= "josedavid"
#bebe=itertools.permutations(palabra)
#print(list(bebe))

""" def permutation(word:str):
    if len(word)==1:#caso base
        return [word]
    l = []
    for j in range(len(word)):   
        letter = word[j]     
        rest = word[:j]  +word[j+1:] 
        
        for i in permutation(rest):
            l.append(letter+i)
    
    return l  """
    
""" 
print(permutation('jsoedavidsadafasf'))
 """
 
#hacer el triangulo de pascal

""" lista= []
l=0 
for i in range(5): 
    lista.append(1)
    print(lista)
    if len(lista)>1:
        for j in range(len(lista)-1):
            valor=lista[j+1]
            lista[j+1]=lista[j+1] + lista[j-1]
  
print(lista)
             """

""" 
def practicando(lista:list):  
    lista.append(1)
    print(lista)
    for i in range(1,5):
        for j in range(len(lista)-1,0,-1):
            lista[j]= lista[j]+ lista[j-1]
        lista.append(1)
        print(lista)
            
practicando([]) """