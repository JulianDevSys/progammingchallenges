""" 
from os import system
from time import sleep


fila = ['*', '*', '*', ' ', ' ', ' ', ' ', ' ']


for i in range(100000):
    fila.append(fila.pop(0))
    print(fila)
    sleep(0.5)
    system('cls')
 """

# Dado un arreglo de numeros enteros eliminar los repetidos no se vale usar set(conjuntos)
l1 = [1, 2, 2, 5, 3, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 3]  # 1,2,3,4,5,6
# Solucion 1
limit = len(l1)
i = 0
while i < limit:
    j = i+1
    while j < limit:
        if l1[i] == l1[j]:
            l1.pop(j)
            limit -= 1
            continue
        j += 1
    i += 1

print(l1)
# Solucion 2
l3 = []
for i in l1:
    if i not in l3:
        l3.append(i)

print(l3)
# solucion 3
l4 = []
l1 = [1, 2, 2, 5, 3, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 3]  # 1,2,3,4,5,6
for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] == l1[j] and l1[j] != '*':
            l1[j] = '*'
for i in l1:
    if i != '*':
        l4.append(i)
print(l1, l4)

# solicion 4
l1 = [1, 2, 2, 5, 3, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 3]  # 1,2,3,4,5,6
dic = dict()
for i in l1:
    dic[i] = 1
print(list(dic.keys()), dic)


# solucion 5
print(list(set(l1)))
