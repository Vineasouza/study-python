"""
Map function
"""

def dobro(x_param):
    """Retorna o dobro."""
    return x_param*2

VALOR_LIST  = [1,2,3,4,5]

print(list(map(dobro, VALOR_LIST)))
