arquivo = open("arquivo.txt")

#readline le uma linha
#readlines le o arquivo e armazena em uma lista
linhas = arquivo.readlines()
print(linhas)

for linhas in linhas:
    print(linhas)

#read le o arquivo inteiro
textoCompleto = arquivo.read()
print(textoCompleto)

#manipulando - criando arquivo
w = open("arquivo2.txt", "w")
#escrevendo no arquivo
w.write("esse e meu arquivo\n")
#fechar arquivo
w.close()

#manipulando - abrindo arquivo pra escrita
w = open("arquivo2.txt", "a")
w.write("esse e meu arquivo\n")
w.close()