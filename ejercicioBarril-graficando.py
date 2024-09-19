# enunciado
""" realice un algoritmo para simular el precio del barril de petroleo durante un mes de 30 dias, suponiendo que son valores enteros
que fluctuan en forma aleatoria entre 130 y 150 , obtenga las siguientes respuestas
1) el promedio del precio del petroleo
2) en que dia estuvo mas barato el barril del petroleo
3) graficar el cambio del precio del petroleo en un mes """

import random
import math

# para poder graficar
import matplotlib.pyplot as mat


# primera forma de hacerla
def precio_barril():
    test = math.inf
    dia_barato = test
    total = 0
    dia = 0
    numeros = []
    petroleo_valor = []
    cantidad_dias = 31
    for i in range(1, cantidad_dias):
        numeros.append(i)
        valor_petroleo = random.randint(130, 150)
        petroleo_valor.append(valor_petroleo)
        if dia_barato > valor_petroleo:
            dia_barato = valor_petroleo
            dia = i
        total += valor_petroleo
    promedio = total / cantidad_dias
    # colcca los puntos de la grafica
    mat.scatter(numeros, petroleo_valor)
    # grafica
    mat.plot(numeros, petroleo_valor, label="precio")
    #
    mat.legend()
    mat.show()
    return f"el promedio es de: {promedio} el dia mas barato es: {dia_barato} que es el dia {dia}"


# print(precio_barril())


# segunda forma de hacerla
def segundaForma_barril():
    valores = []
    arrelo_dias = []
    total = 0
    cantidad_dias = 31
    i = 1
    while i < cantidad_dias:
        valor_petroleo = random.randint(130, 150)
        valores.append(valor_petroleo)
        arrelo_dias.append(i)
        total += valor_petroleo
        i += 1
    promedio = total / cantidad_dias
    dia_menor = min(valores)
    valor_minimo = valores.index(dia_menor) + 1

    # colcca los puntos de la grafica
    mat.scatter(arrelo_dias, valores)
    # grafica
    mat.plot(arrelo_dias, valores, label="precio")
    #
    mat.legend()
    mat.show()
    return f"el promedio es : {promedio} y el valor menor es: {dia_menor} en el dia: {valor_minimo}"


print(segundaForma_barril())
