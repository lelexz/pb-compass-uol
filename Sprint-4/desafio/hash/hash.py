import hashlib

while True:
    entrada = input("Digite algo: ")
    hash = hashlib.sha1(entrada.encode()).hexdigest()
        
    print("O hash SHA-1 da string digitada é: ", hash)
