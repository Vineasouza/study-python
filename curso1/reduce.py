"""
Using reduce module
"""
from functools import reduce

def soma(x_param,y_param):
    """Retorna a soma de dois parametros."""
    return x_param+y_param

lista = [1,3,5,10,20]

soma = reduce(soma,lista)
print(soma)
