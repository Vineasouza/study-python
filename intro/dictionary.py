#criando dicionario
meu_dicionario = {
    "A" : "AMEIXA",
    "B" : "BOLA",
    "C" : "CACHORRO"
}

print(meu_dicionario)
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])

for i in meu_dicionario:
    print(i+" : "+meu_dicionario[i])

#funcoes
for i in meu_dicionario.items():
    print(i)

for i in meu_dicionario.values():
    print(i)

for i in meu_dicionario.keys():
    print(i)