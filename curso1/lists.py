"""
List comparison
"""

#cricao de listas
MINHA_LISTA = ["abacaxi", "melancia", "abacate"]
MINHA_LISTA2 = [1,2,3,4,5]
MINHA_LISTA3 = ["abacaxi", 2, 9.89, True]

#printando listas inteiras
print(MINHA_LISTA)
print(MINHA_LISTA2)
print(MINHA_LISTA3)

#printando valor especifico
print(MINHA_LISTA[1])

#varrendo LISTA
for i in MINHA_LISTA:
    print(i)

#tamanho da LISTA
TAM = len(MINHA_LISTA)
print(TAM)

#adicionar elementos ao final da LISTA
MINHA_LISTA.append("limao")
print(MINHA_LISTA)

#localizar elementos na LISTA
if 7 in MINHA_LISTA2:
    print("7 esta na LISTA")
else:
    print("7 nao esta na LISTA")

#remover elementos na LISTA
del MINHA_LISTA[2:]
print(MINHA_LISTA)

#criar LISTA em branco
MINHA_LISTA4 = []
MINHA_LISTA4.append(57)
print(MINHA_LISTA4)

#ordenacao de listas
LISTA = [4,7,6,9,23,45,1,5,87,200]
print(LISTA)
#inverter a ordem a LISTA
LISTA.reverse()
print(LISTA)
#retorna a LISTA ordenada
LISTAORD = sorted(LISTA)
print(LISTAORD)
#ordena a LISTA
LISTA.sort()
print(LISTA)
#ordena a LISTA decrescente
LISTA.sort(reverse=True)
print(LISTA)
