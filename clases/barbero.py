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