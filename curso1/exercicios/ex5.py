"""
Escreva um programa que receba dois números e um sinal,
e faça a operação matemática definida pelo sinal.
"""

NUM_1 = float(input("Digite o primeiro valor: "))
NUM_2 = float(input("Digite o segundo valor: "))
OPERADOR = input("Digite o operador: ")

if OPERADOR == '+':
    print("Soma: ", (NUM_1+NUM_2))
elif OPERADOR == '-':
    print("Subtracao: ", (NUM_1-NUM_2))
elif OPERADOR == '*':
    print("Multiplicao: ", (NUM_1*NUM_2))
elif OPERADOR == '/':
    print("Divisao: ", (NUM_1/NUM_2))
else:
    print("Operador nao identificado")
    