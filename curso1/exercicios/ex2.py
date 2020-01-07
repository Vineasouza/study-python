#Faça um programa que receba duas notas digitadas
#pelo usuário. Se a nota for maior ou igual a seis, 
# escreva aprovado, senão escreva reprovado. 

p1 = float(input("Digite sua nota da P1: "))
p2 = float(input("Digite sua nota da P2: "))
media = ((p1+p2)/2)

if media >= 6.0:
    
    print("APROVADO com media: ", media)
else:
    print("REPROVADO com media: ", media)
    
