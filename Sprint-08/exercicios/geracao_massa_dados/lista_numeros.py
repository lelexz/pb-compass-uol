import random

numeros_lista = [random.randint(1, 500) for _ in range (250)] 
numeros_lista.reverse()

print(numeros_lista)