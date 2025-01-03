with open('actors.csv', 'r', encoding='latin-1') as arquivo:
    with open('etapa3.txt', 'w', encoding='utf-8') as saida:
        ator = ""
        maior_media = -1
        
        next(arquivo)  
        
        for linha in arquivo:
            if '"Robert Downey, Jr."' in linha: 
              linha = linha.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
            dados = linha.strip().split(',')
            
            nome = dados[0]
            media = float(dados[3])
            
            if media > maior_media:
                maior_media = media 
                ator = nome  
        
        print(f"O ator com maior número de bilheteria é: {ator} com média de {maior_media}", file=saida)
