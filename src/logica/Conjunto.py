def __init__(self):
    self.numeros = []


def agregar_numero(self, numero):
    self.numeros.append(numero)


def calcular_promedio(self):
    if not self.numeros:
        return 0
    return sum(self.numeros) / len(self.numeros)