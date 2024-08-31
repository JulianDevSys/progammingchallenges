""" /*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */ """
 
"""  
def countword(word):
    contador= 0
    print(word.split(" "))
    
    for i in range(word):
        for j in word:
            if i == j:
                contador+= 1
            else:
                
            
print(countword("hola como Estas")) """