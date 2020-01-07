#Escreva um programa que ordene uma lista numérica com três elementos

lista = [3,2,1]

#bubblesort
def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[ j ] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(lista)
print(bubble_sort(lista))