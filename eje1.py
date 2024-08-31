""" /*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */ """
 

def tranformar_pulsaciones(palabra_clave):
    texto_desincriptado=[]
    diccionario={
        "3":"d",
        "33": "e",
        "888": "v",
        "6": "m",
        "666":"o",
        "88":"u",
        "777":"r",
        
    }
    resultado= palabra_clave.split("-") 
    for i in range(len(resultado)):
        if resultado[i] in diccionario:
            texto_desincriptado.append(diccionario[resultado[i]])
    return "".join(texto_desincriptado).upper()       
            
print(tranformar_pulsaciones("6-666-88-777-33-3-33-888"))  
print(tranformar_pulsaciones("5-88-555-444-2-66"))         
            
            
            
def t9(n):
    diccionario={
        "2":"abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6":"mno",
        "7":"pqrs",
        "8":'tuv',
        "9":'wxyz'        
    }
    r = n.split('-')
    output = ''
    for j in r:
        output+= diccionario[j[0]][len(j)-1]
    return output       
            
print(t9("6-666-88-777-33-3-33-888"))
print(t9("5-88-555-444-2-66")) 
            
        
        
 