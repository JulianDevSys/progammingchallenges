import random
import math


contador=0
contador1=0
for i in range(1,7):
    for j in range(1,7):
        if  i+j >7 :
            contador+=1
        if math.fabs(j-i)<2:
            contador1+=1
            
if contador>contador1:
    print("el ganador es pedro")
else :
    print(f"el ganador es pablo, las posibilidades son:  {contador1} y las de pedro son: {contador}")

#probabilidad moneda
contador= 0
contador2=0
probaabilidad= ["cara", "sello"]
for i in range(100):
    eleccion= random.choice(probaabilidad)
    if eleccion== "cara":
        contador+=1
    else:
        contador2+=1
    
print(f"la cantidad de veces que salio caras es: {contador}")
print(f"la cantidad de veces que salio sellos es: {contador2}") 


#///////////////////////////////////3


import simpy

class InventorySystem:
    def _init_(self, env):
        self.env = env
        self.inventory = 10  # Inicialmente, hay 10 productos en el inventario
        self.out_of_stock_event = env.event()  # Evento de agotamiento de productos

    def generate_products(self, rate):
        while True:
            # Generar un producto cada 5 minutos
            yield self.env.timeout(5 / rate)
            self.inventory += 1
            print(f"{self.env.now}: Generado un producto. Total en inventario: {self.inventory}")

    def check_out_of_stock(self):
        while True:
            # Verificar si el inventario se ha agotado cada minuto
            yield self.env.timeout(1)
            if self.inventory == 0:
                self.out_of_stock_event.succeed()  # Activar el evento de agotamiento de productos
                print(f"{self.env.now}: El producto se ha agotado.")
                self.out_of_stock_event = self.env.event()  # Reiniciar el evento

    def process_orders(self, rate):
        while True:
            # Procesar un pedido cada 3 minutos
            yield self.env.timeout(3 / rate)
            if self.inventory > 0:
                self.inventory -= 1
                print(f"{self.env.now}: Procesado un pedido. Total en inventario: {self.inventory}")
            else:
                print(f"{self.env.now}: No hay productos disponibles.")

    def run(self, rate):
        self.env.process(self.generate_products(rate))
        self.env.process(self.check_out_of_stock())
        self.env.process(self.process_orders(rate))
        self.env.run(until=50)  # Ejecutar la simulación durante 50 unidades de tiempo

env = simpy.Environment()
inventory_system = InventorySystem(env)
inventory_system.run(rate=1)  # Tasa de generación de productos por minuto