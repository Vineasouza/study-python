"""
Escreva um programa que ordene uma lista numérica com três elementos
"""

LISTA = [3,2,1]

#bubblesort
def bubble_sort(lista):
    """Bubble sort"""
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
            if lista[ j ] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(LISTA)
print(bubble_sort(LISTA))
