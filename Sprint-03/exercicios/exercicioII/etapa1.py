
with open('actors.csv', encoding='latin-1') as arquivo:
    with open('etapa1.txt', 'w', encoding='utf-8') as saida:
        ator = ""
        maior_num_filmes = -1
        
        next(arquivo)  
        
        for linha in arquivo:
            if '"Robert Downey, Jr."' in linha:
                    linha = linha.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
            dados = linha.strip().split(',')
            
            
            nome = dados[0]
            qtd_filme = int(dados[2])
            
            if qtd_filme > maior_num_filmes:
                maior_num_filmes = qtd_filme
                ator = nome  
        
        print(f"O ator com maior número de filmes é: {ator} com {maior_num_filmes} filmes", file=saida)
    
