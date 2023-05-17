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

