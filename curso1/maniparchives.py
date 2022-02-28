"""
Manipulando arquivos de arquivos
"""

with open("arquivo.txt", encoding="utf8") as ARQUIVO_1:
    #readline le uma linha
    #readlines le o arquivo e armazena em uma lista
    LINHAS = ARQUIVO_1.readlines()
    print(LINHAS)

    for LINHAS in LINHAS:
        print(LINHAS)

    #read le o arquivo inteiro
    TEXTO_COMPLETO = ARQUIVO_1.read()
    print(TEXTO_COMPLETO)

#manipulando - criando arquivo
with open("arquivo2.txt", "w", encoding="utf8") as ARQUIVO_2:
    #escrevendo no arquivo
    ARQUIVO_2.write("esse e meu arquivo\n")


#manipulando - abrindo arquivo pra escrita
with open("arquivo2.txt", "a", encoding="utf8") as ARQIVO_3:
    ARQIVO_3.write("esse e meu arquivo\n")
