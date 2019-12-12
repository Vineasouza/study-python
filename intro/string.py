a = "Vinicius"
b = "Souza"

concat = a + " " + b + "\n"
print(concat)
tamanho = len(concat)
print(tamanho)

print(concat[0:14])

##metodos##

#deixa tudo em caixa baixa
print(concat.lower())

#deixa tudo de caxa alta
print(concat.upper())

#remove espaços
print(concat.strip())

#quebra uma string no que e definido
string = "O rato roeu a roupa do rei de Roma"
string = string.split(" ")
print(string)

#busca de substring
string = "O rato roeu a roupa do rei de Roma"
busca = string.find("rei")
print(busca)
print(string[busca:])

#substitui string
print(string.replace("o rei", "a rainha"))

