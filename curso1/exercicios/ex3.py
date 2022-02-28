"""
Escreva um programa que resolva uma equação de segundo grau.
"""

from math import sqrt

VAR_A = float(input("Digite o valor de VAR_A: "))
VAR_B = float(input("Digite o valor de VAR_B: "))
VAR_C = float(input("Digite o valor de VAR_C: "))

DELTA = VAR_B**2 - 4*VAR_A*VAR_C
RAIZ_DELTA = sqrt(DELTA)

RAIZ_1 = (-VAR_B + RAIZ_DELTA)/2*VAR_A
RAIZ_2 = (-VAR_B - RAIZ_DELTA)/2*VAR_A

print("Raiz 1: ", RAIZ_1)
print("Raiz 2: ", RAIZ_2)
