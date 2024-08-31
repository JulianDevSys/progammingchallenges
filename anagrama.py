""" /*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */ """
 
   
""" 
def anagrama(palabra1,palabra2):
    if palabra1.upper()== palabra2.upper() or len(palabra1) != len(palabra2):
        return "no son anagramas"
    for i in range (len(palabra1)):
        if palabra1[i] not in palabra2:
            print("no es un anagrama")
            anagramas=False
            break
        else:
            anagramas= True    
        
    if anagramas== True:
        print(f"las palabras {palabra1} y {palabra2} son anagramas")
        
        
        
print(anagrama("cara", "raca"))  """