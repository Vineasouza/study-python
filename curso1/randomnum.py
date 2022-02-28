"""
Usuing random module
"""

import random

#gera numero aleatorio no intervalo definido
num = random.randint(0,10)
print(num)

#escolhe um numero aleatorio na lista
lista= [6, 45, 9]
num = random.choice(lista)
print(num)

#shuffle
print("Lista original : ",lista)
random.shuffle(lista)
print("Shuffle : ", lista)
