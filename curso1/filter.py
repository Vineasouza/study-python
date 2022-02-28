"""
Using filter function
"""

def pares(i):
    """Retorna os pares."""
    if i%2==0:
        return i
    return None

def impares(i):
    """Retorna os ímpares."""
    if i%2==1:
        return i
    return None

lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares,lista)
print(list(lista_pares))

lista_impares = filter(impares,lista)
print(list(lista_impares))
