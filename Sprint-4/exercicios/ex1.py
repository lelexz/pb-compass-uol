def ler_numeros(num):
    with open("number.txt", "r") as arquivo:
        return [int(line.strip()) for line in arquivo]

num = "number.txt"

numeros = ler_numeros(num)

maiores_pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)[
    :5
]
maiores_pares = list(map(int, maiores_pares))

soma = sum(maiores_pares)

print(maiores_pares)
print(soma)