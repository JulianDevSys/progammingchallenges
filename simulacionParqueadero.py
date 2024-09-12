import simpy
import math
import random

SEMILLA = 30
NUM_cupos = 10
tiempo_Parqueo_MIN = 5
tiempo_Parqueo_MAX = 150
T_LLEGADAS = 5  # Tiempo entre llegadas de vehículos
TIEMPO_SIMULACION = 220
TOT_vehiculos = 100
dt = 0.0  # Duración de servicio total
fin = 0.0  # Minuto en el que finaliza
TIEMPO_ESPERA_MAXIMO = 5  # Tiempo máximo de espera permitido

def parking(vehiculo):
    global dt
    R = random.random()  # Obtiene un número aleatorio
    tiempo = tiempo_Parqueo_MAX - tiempo_Parqueo_MIN
    tiempo_parqueo = tiempo_Parqueo_MIN + (tiempo * R)  # Distribución uniforme
    yield env.timeout(tiempo_parqueo)  # Deja correr el tiempo n minutos
    print(" \o/ Carro parqueado a %s en %.2f minutos" % (vehiculo, tiempo_parqueo))
    dt += tiempo_parqueo  # Acumula los tiempos de uso

def vehiculo(env, name, personal):
    global fin
    llega = env.now  # Guarda el minuto de llegada del vehículo
    print("---> %s llegó al parqueadero en minuto %.2f" % (name, llega))
    
    # Intenta obtener acceso al parqueadero, pero si no puede en 5 minutos, abandona
    with personal.request() as request:
        resultado = yield request | env.timeout(TIEMPO_ESPERA_MAXIMO)
        
        # Verifica si el vehículo consiguió un espacio o no
        if request in resultado:
            pasa = env.now  # Minuto en el que entra al parqueadero
            espera = pasa - llega  # Calcula el tiempo que esperó
            print("**** %s pasa al parqueadero en minuto %.2f habiendo esperado %.2f minutos" % (name, pasa, espera))

            yield env.process(parking(name))  # Invoca el proceso de estacionamiento
            deja = env.now  # Guarda el minuto en que deja el parqueadero
            print("<--- %s deja el parqueadero en minuto %.2f" % (name, deja))
            fin = deja  # Conserva globalmente el último minuto de la simulación
        else:
            # Si el tiempo de espera excedió el límite, el vehículo abandona el intento
            print("XXX %s abandonó la fila después de esperar %.2f minutos" % (name, TIEMPO_ESPERA_MAXIMO))

def principal(env, personal):
    for i in range(TOT_vehiculos):
        R = random.random()
        llegada = -T_LLEGADAS * math.log(R)  # Distribución exponencial
        yield env.timeout(llegada)  # Deja transcurrir un tiempo entre llegadas

        env.process(vehiculo(env, "vehiculo %d" % (i + 1), personal))  # Inicia el proceso para cada vehículo

print("<------------------- Bienvenido Simulación De Parqueadero ------------------>")
random.seed(SEMILLA)  # Fija la semilla para reproducibilidad
env = simpy.Environment()  # Crea el objeto entorno de simulación
personal = simpy.Resource(env, NUM_cupos)  # Crea los recursos (parqueadero)
env.process(principal(env, personal))  # Invoca el proceso principal
env.run(until=TIEMPO_SIMULACION)  # Inicia la simulación

# Cálculos y resultados
print("\n---------------------------------------------------------------------")
print("\nIndicadores obtenidos: ")
lpc = 0  # No se calcula lpc ya que no se está acumulando te
upi = (dt / fin) / NUM_cupos  # Uso promedio de la instalación
print("Uso promedio de la instalación = %.2f" % upi)
print("\n---------------------------------------------------------------------")
