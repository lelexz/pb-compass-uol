def my_map(lista, func):
    resultado = []
    for i in lista:
        resultado.append(func(i))
    return resultado
        
def potencia(num):
    return num ** 2

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(entrada, potencia)
print(resultado)