animais_lista = ["leão",
           "cavalo",
           "gato",
           "onça",
           "girafa",
           "baleia",
           "coelho",
           "cachorro",
           "zebra",
           "pato",
           "galinha",
           "pavão",
           "ovelha",
           "cabra",
           "porco",
           "avestruz",
           "lhama",
           "camelo",
           "tubarão",
           "hipopótamo"]

animais_lista.sort()

for animal in animais_lista:
    print(animal)
    
with open("animais.csv", "w", encoding="utf-8") as arquivo:
    for animal in animais_lista:
        arquivo.write (f"{animal}\n" )