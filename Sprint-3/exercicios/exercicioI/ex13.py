arquivo = open('arquivo_texto.txt')
for texto in arquivo:
    print(texto, end='')
arquivo.close