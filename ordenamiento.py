
     
#metodo burbuja     
lista= [5, 3, 8, 4,11, 2,1,10,0,-5,2,-2,-7,67,-12,2,4,5,100,2,1,0,-20,15,-1,4,-4]
tamaño= len(lista)
pasos=0
for l in range(tamaño-1):
    pasos+=1
    for i in range(tamaño-1):
        pasos+=1
        j=i+1
        if lista[i]> lista[j]:
            orden= lista[j]
            lista[j]= lista[i]
            lista[i]=orden
    tamaño-=1
print(lista)
print(pasos)
 

 #ordenamiento insertion sort
#print(lista_ordenada)
lista_no_ordenada= [5, 3, 8, 4,11, 2,1,10,0,-5,2,-2,-7,67,-12,2,4,5,100,2,1,0]
lista_ordenada=[]
lista_ordenada.append(lista_no_ordenada[0])
tamaño=len(lista_no_ordenada)
pasos= 0
for i in range(1,tamaño):
    pasos+=1
#paso:1 unir el elemento i en el nuevo arreglo
    lista_ordenada.append(lista_no_ordenada[i])
    tamaño1=len(lista_ordenada)
#paso2. comparar cual es mayor

    for j in range(tamaño1-1,0,-1):
        pasos+=1
        l=j-1
        if lista_ordenada[j]< lista_ordenada[l]: 
            orden= lista_ordenada[l]  
            lista_ordenada[l]=lista_ordenada[j]
            lista_ordenada[j]=orden
        #print(lista_ordenada)
        
print(pasos) 



#////////////////////////[5, 3, 8, 4,11, 2,1,10,0,-5,2,-2,-7,67]

#/// insertion sort

lista= [5, 3, 8, 4,11, 2,1,10,0,-5,2,-2,-7,67,-12,2,4,5,100,2,1,0,-20,15,-1,4,-4]
pasos= 0
for i in range(1,len(lista)):
    pasos+=1
    orden= lista[i]
    j=i-1
    while j >=0 and orden <lista[j]:
        pasos+=1
        lista[j+1]= lista[j]
        j-=1
    lista[j+1]=orden
        


print(lista)
print(pasos)
    