"""
Faça um programa que receba duas notas digitadas
pelo usuário. Se a nota for maior ou igual a seis,
escreva aprovado, senão escreva reprovado.
"""

NOTA_P1 = float(input("Digite sua nota da P1: "))
NOTA_P2 = float(input("Digite sua nota da P2: "))
NOTA_MEDIA = ((NOTA_P1+NOTA_P2)/2)

if NOTA_MEDIA >= 6.0:
    print("APROVADO com media: ", NOTA_MEDIA)
else:
    print("REPROVADO com media: ", NOTA_MEDIA)
    