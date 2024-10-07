import csv

def resultado_notas(arquivo):
    resultado = {}

    with open(arquivo, "r") as nomes:
        leitor_csv = csv.reader(nomes)
        
        for linha in leitor_csv:
            nome, *notas_str = linha
            notas = list(map(int, notas_str))
            notas_desc = sorted(notas, reverse=True)[:3]
            resultado[nome] = notas_desc

    return resultado

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return round(media, 2)

def resultado_ordenado(resultado):
    ordenado = sorted(resultado.items(), key=lambda x: x[0])
    
    for nome, notas in ordenado:
        media = calcular_media(notas)
        print(f"Nome: {nome} Notas: {notas} Média: {media}")

arquivo = "estudantes.csv"
resultado = resultado_notas(arquivo)
resultado_ordenado(resultado)