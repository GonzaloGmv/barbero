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