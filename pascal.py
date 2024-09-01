#hacer el triangulo de pascal
 
def practicando(lista:list):  
    lista.append(1)
    print(lista)
    for i in range(1,5):
        for j in range(len(lista)-1,0,-1):
            lista[j]= lista[j]+ lista[j-1]
        lista.append(1)
        print(lista)
            
practicando([]) 