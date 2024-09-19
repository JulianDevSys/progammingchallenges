""" Estación de Carga con Prioridades y Mantenimiento
Imagina que ahora la estación de carga de autos eléctricos tiene 4 puntos de carga y debe lidiar con lo siguiente:

Requisitos: Llegada de autos: Los autos llegan a la estación cada 3 minutos. 
La estación tiene 20 autos para simular en total.
Los autos se dividen en dos tipos: Autos comunes, que llegan cada 3 minutos.
Autos prioritarios (taxis eléctricos), que tienen mayor prioridad en la fila. Estos llegan cada 6 minutos.

Tiempo de carga: Los autos comunes tardan entre 25 y 50 minutos en cargar.
Los autos prioritarios tardan entre 15 y 40 minutos.

Sistema de prioridad:
Si un auto prioritario llega a la estación y no hay puntos de carga disponibles,
desplaza al primer auto común que aún esté esperando.
Si un auto espera más de 20 minutos, se va sin cargar.
Mantenimiento de los puntos de carga:

Cada hora, un técnico cierra un punto de carga para mantenimiento durante 15 minutos, lo que reduce temporalmente la capacidad de la estación.
Simulación:

La simulación debe ejecutarse durante 250 minutos. """

import simpy
import random
import simpy.resources


# creamos la funcion de la estacion de carga
def estacion_carga(env, carros, zona_carga, tipo_vehiculo):
    hora_llegada_autmovil = env.now

    if tipo_vehiculo == "comunes":
        tiempo_carga = random.randint(25, 50)
    else:
        tiempo_carga = random.randint(15, 40)

    print(
        f"el {carros} {tipo_vehiculo} acaba de llegar a la zona de carga a los {env.now} minutos"
    )
    # Si un auto prioritario llega a la estación y no hay puntos de carga disponibles,desplaza al primer auto común que aún esté esperando
    # lo que hacemos es pasarle al request priority= 0 el cual significa que es alta prioridad si el tipo de vehivulo es uno sino 1 que es baja prioridad
    with zona_carga.request(
        priority=0 if tipo_vehiculo == "prioritarios" else 1
    ) as reqZona_carga:
        yield reqZona_carga
        tiempo_espera = env.now - hora_llegada_autmovil

        if tiempo_espera > 20:
            return print(
                f"{carros} {tipo_vehiculo} se fue porq lleva esparando mas de 20 minutos en la fila"
            )
        else:
            print(
                f"{carros} {tipo_vehiculo} entro a la zona de carga a los {tiempo_espera} minutos en la fila"
            )

        yield env.timeout(tiempo_carga)
        print(
            f"el {carros} {tipo_vehiculo} salio de la zona de carga a los {env.now} minutos"
        )


# declaramos los automoviles comunes con las especificaciones del enunciado
def autmoviles_comunes(env, zona_carga):
    llegada_automoviles_comunes = 3
    cantidad_autos = 11
    for i in range(1, cantidad_autos):
        yield env.timeout(llegada_automoviles_comunes)
        env.process(
            estacion_carga(env, f" autmoviles comunes {i}", zona_carga, "comunes")
        )


# declaramos los automoviles prioritarios con las especificaciones del enunciado
def automoviles_prioritarios(env, zona_carga):
    llegada_automoviles_prioritarios = 6
    cantidad_autos = 11
    for i in range(1, cantidad_autos):
        yield env.timeout(llegada_automoviles_prioritarios)
        env.process(
            estacion_carga(
                env, f" autmoviles prioritarios {i}", zona_carga, "prioritarios"
            )
        )


# colocamos en manteniemiento el punto de carga dejando una capacidad de 3
def mantenimiento_zonaCarga(env, zona_carga):
    # para que se reita siempre, mientras corre el ambiente
    while True:
        hora = 60
        tiempo_mantenimiento = 15
        yield env.timeout(hora)
        print(
            f"un técnico cierra un punto de carga para mantenimiento durante 15 minutos a los {env.now} minutos"
        )
        zona_carga.capacity -= 1
        yield env.timeout(tiempo_mantenimiento)
        zona_carga.capacity += 1
        print(f"el punto de carga vuelve a estar disponible en el minuto {env.now}")


# creamos en el ambiente y procesos
env = simpy.Environment()
zona_carga = simpy.Resource(env, capacity=4)
env.process(autmoviles_comunes(env, zona_carga))
env.process(automoviles_prioritarios(env, zona_carga))
env.process(mantenimiento_zonaCarga(env, zona_carga))
env.run(250)
