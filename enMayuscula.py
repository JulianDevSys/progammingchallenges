""" /*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */ """
 

def firstMayuscula(word):
    nuevo_arreglo=[]
    arreglo= word.split(" ")
    for i in range(len(arreglo)):
        nuevo_arreglo.append(arreglo[i][0].upper()+ arreglo[i][1:])
    return " ".join(nuevo_arreglo)
        
print(firstMayuscula("voy a ser el mejor programador del mundo"))