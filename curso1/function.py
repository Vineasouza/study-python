"""
Using functions as arguments
"""

def soma(x_param,y_param):
    """Retorna a soma."""
    return x_param+y_param

def mul(x_param,y_param):
    """Retorna a multiplicacao."""
    return x_param*y_param

print("SOMA", soma(2,3))
print("MULTIPLICACAO", mul(2,3))

print(soma(soma(2,3),mul(2,3)))
