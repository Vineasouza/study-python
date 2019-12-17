#Funcao zip

lista1 = [1,2,3,4,5]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante"]
lista3 = [2.00, 5.00, 10.00, 20.00]

for num,nome,valor in zip(lista1, lista2,lista3):
    print(num, nome, valor)