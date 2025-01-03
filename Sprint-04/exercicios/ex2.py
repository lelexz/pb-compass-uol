def conta_vogais(texto:str)-> int:
    vogais = "aeiou"

    vogais_presentes = filter(lambda letras: letras in vogais, texto.lower())
    return len(list(vogais_presentes))
    

resultado = conta_vogais("testando")
print(resultado)