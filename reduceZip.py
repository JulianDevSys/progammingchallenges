from functools import reduce

lista1 = [1,2,3,34,5,6,7,8]

lista2 =  list(map(lambda x,y:str(x)+"*-"+str(y),lista1,lista1))

print(lista2)



lista3 = [1,2,3,4,5,6,7]

lista4 = [1,2,3,4,5,6,7,2,3,4,4,5,5,6,67]

lista5 =  list(zip(lista3,lista4,lista4))
print(lista5)


#hacer una funcion que reciba un arreglo y este retorne la suma de solo sus numero impares


lista10=[1,3,5,7,11,13,4,8,10]

reducir= reduce(lambda x,y : x+ y,filter(lambda x: x%2 != 0, lista10))
print(reducir)