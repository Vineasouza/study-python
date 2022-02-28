"""
Foo
"""

LISTA_1 = [1,2,3,4,5]
LISTA_2 = ["abacate","bola","cachorro","dinheiro","elefante"]
LISTA_3 = [2.00, 5.00, 10.00, 20.00]

for num,nome,valor in zip(LISTA_1, LISTA_2,LISTA_3):
    print(num, nome, valor)
