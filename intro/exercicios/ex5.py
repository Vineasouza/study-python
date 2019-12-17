#Escreva um programa que receba dois números e um sinal, 
#e faça a operação matemática definida pelo sinal.

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
op = input("Digite o operador: ")

if op == '+':
    print("Soma: ", (num1+num2))
elif op == '-':
    print("Subtracao: ", (num1-num2))
elif op == '*':
    print("Multiplicao: ", (num1*num2))
elif op == '/':
    print("Divisao: ", (num1/num2))
else:
    print("Operador nao identificado")