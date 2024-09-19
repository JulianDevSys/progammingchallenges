
import simpy
import simpy.resources
import random

#entorno donde ocurren los eventos env= simpy.environment()
#env.now (now--> nos muestra el instante de tiempo en el que nos encontramps)

""" 
def proceso(env):
    print(f"inicio del proceso en t= {env.now}")
    yield env.timeout(10)
    print(f"proceso reanudado en t= {env.now}")


env=simpy.Environment()
env.process(proceso(env))
env.run()
 """
######################################################################################################################
""" def tarea(has):
    while env.now +5 <=20:
        print(f"la tarea comienza a los {has.now} minutos")
        yield has.timeout(5)
        print(f"la tarea fue terminada en  {has.now} minutos")
    
    
env= simpy.Environment()
#yield es un proceso y para que se ejecute necesitamos usa el env.process(la funcion(env))
env.process(tarea(env))
env.run(until= 21) """

#######################################################################################################################

""" def productor(env, event):
    yield env.timeout(5)
    event.succeed()
    print(f"pago finalizado en el minuto {env.now}")
    
def consumidor(env, event):
    print(f"realizando el pago en el minuto {env.now} ")
    yield event

def despedir(env, event):
    yield event
    print(f"muchas gracias por todo hasta luego {env.now}")
    

env= simpy.Environment()
evento= env.event()
env.process(productor(env,evento))
env.process(consumidor(env,evento))
env.process(despedir(env,evento))

env.run(10) """


##########################################################################################################################
#recursos representan una cantidad limitada, que puede ser compartida entre varios procesos se representa con el req

""" def cliente(env, nombre, cajero):
    print(f"{nombre} llego al cajero en el minuto {env.now} ")
    with cajero.request()as req:
        yield req
        print(f"{nombre} comienza a usar el cajero en el minuto {env.now}")
        yield env.timeout(5)
        print(f"{nombre} ha terminado de usar el cajero en el minuto {env.now}")
        

env=simpy.Environment()
cajero= simpy.Resource(env, capacity= 1)
env.process(cliente(env,"cliente1", cajero))
env.process(cliente(env,"cliente2", cajero))
env.process(cliente(env,"cliente 3", cajero))

env.run(20)
 """
 
#terminar ejercicio despues, ir mejorando el codigo
#777777777777777777777777777777777777777777777777777777777777777777

def parqueadero(env, car, parking):
    salida_automovil= random.randint(10,50)
    tiempoEn_fila=10
    time_arrive= env.now
    print(f"el {car} llego al parqueadero en {time_arrive}")
    with parking.request() as reqParqueo:
        yield reqParqueo
        time_espera= env.now- time_arrive
        if time_espera <= tiempoEn_fila :
            print(f"el {car} entro al parquedero {env.now}, esperó {time_espera} minutos para entrar")
        else:
            return print (f"el {car} salio de la fila, esperó mucho tiempo, espero mas de 10 minutos")
            
        yield env.timeout(salida_automovil)
        print(f"el {car} salio del parqueadero a las {env.now}")

def automoviles (env,park):
    timpo_llegada_automoviles=5
    cantidad_carros= 30
    for i in range (1,cantidad_carros):
        env.process(parqueadero(env, f"automovil {i}", parking))
        yield env.timeout(timpo_llegada_automoviles)
    

env= simpy.Environment()
parking= simpy.Resource(env, capacity=5)
env.process(automoviles(env, parking))

env.run(250) 


#7 practicando 
# with == resourse.release

""" def peluqueria(env, nombre, peluqueros):
    tiempo_llegda= env.now
    salida_peluqueria= random.randint(15, 40)
    
    print(f"{nombre } ha llegado a la peluqueria {tiempo_llegda}")
    with peluqueros.request() as peluquerosDisponibles:
        yield peluquerosDisponibles 
        tiempo_espera= env.now- tiempo_llegda       
        print(f"{nombre} a entrado a la peluqueria a{env.now} minutos. esperó {tiempo_espera} minutos")
        yield env.timeout(salida_peluqueria)
        print(f"{nombre} salio de la peluqueria a {env.now}")


env= simpy.Environment()

peluqueros= simpy.Resource(env,capacity=2)
env.process(peluqueria(env,"julian", peluqueros))
env.process(peluqueria(env,"esteban", peluqueros))
env.process(peluqueria(env,"sergio", peluqueros))
env.process(peluqueria(env,"luis M", peluqueros))

env.run(150) """






