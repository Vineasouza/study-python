"""
Using exception function
"""

A = 2
B = 1

try:
    print(A/B)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    