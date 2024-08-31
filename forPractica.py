lista = ["jose", "julian", "esteban", "david"]
for nombre in lista:
    print(nombre)

print('----------------------')
for i in range(len(lista)):
    print(lista[i])


print('----------------------')
for i, k in enumerate(lista):
    print(i, k)

print('----------------------')
[i, j, f, c] = lista

print(i, j, f, c)
