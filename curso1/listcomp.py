"""
List comparison
"""

X_PARAM = [1,2,3,4,5]
Y_PARAM = []

for i in X_PARAM:
    Y_PARAM.append(i**2)

print(X_PARAM)
print(Y_PARAM)

#list comprehension
X_PARAM = [1,2,3,4,5]
Y_PARAM = [i**2 for i in X_PARAM]
Z_PARAM = [i for i in X_PARAM if i%2==1]

print(X_PARAM)
print(Y_PARAM)
print(Z_PARAM)
