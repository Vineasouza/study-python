"""
Manipulating strings
"""

A_VAR = "Vinicius"
B_VAR = "Souza"

CONCAT = A_VAR + " " + B_VAR + "\n"
print(CONCAT)
TAM_STR = len(CONCAT)
print(TAM_STR)

print(CONCAT[0:14])

##metodos##

#deixa tudo em caixa baixa
print(CONCAT.lower())

#deixa tudo de caxa alta
print(CONCAT.upper())

#remove espaços
print(CONCAT.strip())

#quebra uma string no que e definido
STR = "O rato roeu a roupa do rei de Roma"
STR = STR.split(" ")
print(STR)

#busca de subSTR
STR = "O rato roeu a roupa do rei de Roma"
STR_BUSCA = STR.find("rei")
print(STR_BUSCA)
print(STR[STR_BUSCA:])

#substitui STR
print(STR.replace("o rei", "a rainha"))
