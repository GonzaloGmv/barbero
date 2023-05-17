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