#cricao de listas
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

#printando listas inteiras
print(minha_lista)
print(minha_lista2)
print(minha_lista3)

#printando valor especifico
print(minha_lista[1])

#varrendo lista
for i in minha_lista:
    print(i)

#tamanho da lista
tam = len(minha_lista)
print(tam)

#adicionar elementos ao final da lista
minha_lista.append("limao")
print(minha_lista)

#localizar elementos na lista
if 7 in minha_lista2:
    print("7 esta na lista")
else:
    print("7 nao esta na lista")

#remover elementos na lista
del minha_lista[2:]
print(minha_lista)

#criar lista em branco
minha_lista4 = []
minha_lista4.append(57)
print(minha_lista4)

#ordenacao de listas
lista = [4,7,6,9,23,45,1,5,87,200]
print(lista)
#inverter a ordem a lista
lista.reverse()
print(lista)
#retorna a lista ordenada
listaord = sorted(lista)
print(listaord)
#ordena a lista
lista.sort()
print(lista)
#ordena a lista decrescente
lista.sort(reverse=True)
print(lista)