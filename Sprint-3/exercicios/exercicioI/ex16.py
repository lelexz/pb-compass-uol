def soma(num):
    num_lista = num.split(",")
    total = 0
    for i in num_lista:
        total += int(i)
    return total

print(soma("1,3,4,6,10,76"))