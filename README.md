# barbero

El link a este repositorio es [github](https://github.com/GonzaloGmv/barbero)

En este proyecto se simula el problema del barbero, el cual ha sido resuelto con hilos y semáforos.

Para hacerlo he hecho 3 clases, y finalmente lo he ejecutado en el main medianteun lanzador:

### Barbería
```
import threading
import time
import random

class Barberia:
    def __init__(self, num_sillas):
        self.num_sillas = num_sillas
        self.silla_barbero = threading.Semaphore(0)
        self.sillas_espera = threading.Semaphore(num_sillas)
        self.mutex = threading.Semaphore(1)

    def entrar(self):
        self.mutex.acquire()
        if self.sillas_espera._value > 0:
            self.sillas_espera.acquire()
            self.mutex.release()
            print(f"Cliente entrando a la barbería... (sillas disponibles: {self.sillas_espera._value})")
            self.silla_barbero.release()
            self.atender()
        else:
            self.mutex.release()
            print(f"La barbería está llena. El cliente se va... (sillas disponibles: {self.sillas_espera._value})")

    def atender(self):
        print("El barbero está cortando el cabello del cliente...")
        time.sleep(random.randint(1, 5))
        print("El barbero ha terminado de cortar el cabello del cliente.")
        self.sillas_espera.release()
```

### Barbero
```
import threading

class Barbero(threading.Thread):
    def __init__(self, barberia):
        threading.Thread.__init__(self)
        self.barberia = barberia

    def run(self):
        while True:
            print("El barbero está durmiendo...")
            self.barberia.silla_barbero.acquire()
            print("El barbero ha sido despertado.")
            self.barberia.atender()
```            

### Cliente
```
import threading
import time
import random

class Cliente(threading.Thread):
    def __init__(self, barberia):
        threading.Thread.__init__(self)
        self.barberia = barberia

    def run(self):
        while True:
            time.sleep(random.randint(1, 5))
            self.barberia.entrar()
```

### Lanzador
```
from clases.barbero import Barbero
from clases.barberia import Barberia
from clases.clientes import Cliente

def main():
    barberia = Barberia(3)
    barbero = Barbero(barberia)
    cliente1 = Cliente(barberia)
    cliente2 = Cliente(barberia)
    cliente3 = Cliente(barberia)
    barbero.start()
    cliente1.start()
    cliente2.start()
    cliente3.start()
```

### Main
```
from lanzador import main

if __name__ == '__main__':
    main()
```    