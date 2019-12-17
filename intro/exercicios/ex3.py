#Escreva um programa que resolva uma equação de segundo grau.  
from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raizDelta = sqrt(delta)

x1 = (-b + raizDelta)/2*a
x2 = (-b - raizDelta)/2*a

print("Raiz 1: ", x1)
print("Raiz 2: ", x2)