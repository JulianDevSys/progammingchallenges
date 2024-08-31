
""" 
 * Crea un función que reciba un texto y retorne la vocal que
 * más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
  """

def vocal_comun(texto):
    maximo_valor= 0
    vocal_mayor= ""
    diccionario_vocales={"A":0, "E":0, "I":0, "O":0, "U":0}
    for i in texto.upper():
        if i in diccionario_vocales:
            diccionario_vocales[i]+=1       
#diccionario.items() se usa cuando se quiere evaluar, llaves y valores               
    for i, valor in diccionario_vocales.items():
        if valor > maximo_valor:
            maximo_valor= valor
            vocal_mayor= i
        if maximo_valor==0:
            return "no hay vocales"
    return vocal_mayor, maximo_valor   


print(vocal_comun("xxx"))