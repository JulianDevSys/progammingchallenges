import itertools
""" /*
 * Crea un programa que sea capaz de generar e imprimir todas las
 * permutaciones disponibles formadas por las letras de una palabra.
 * - Las palabras generadas no tienen por qué existir.
 * - Deben usarse todas las letras en cada permutación.
 * - Ejemplo: sol, slo, ols, osl, los, lso
 */ """

palabra= "josedavid"
#bebe=itertools.permutations(palabra)
#print(list(bebe))

def permutation(word:str):
    if len(word)==1:#caso base
        return [word]
    l = []
    for j in range(len(word)):   
        letter = word[j]     
        rest = word[:j]  +word[j+1:] 
        
        for i in permutation(rest):
            l.append(letter+i)
    
    return l 
    

print(permutation('jsoedavidsadafasf'))
 