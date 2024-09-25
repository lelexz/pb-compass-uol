with open('actors.csv', 'r', encoding='latin-1') as arquivo:
    with open('etapa4.txt', 'w', encoding='utf-8') as saida:
        next(arquivo)
        contagem_filmes = {}
        
        for linha in arquivo:
            if '"Robert Downey, Jr."' in linha: 
              linha = linha.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
            dados = linha.strip().split(',')
            filme = dados[4] 
            
            if filme in contagem_filmes:
                contagem_filmes[filme] += 1
            else:
                contagem_filmes[filme] = 1
                
        filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))
        
        for filme, quantidade in filmes_ordenados:
            print(f'O filme {filme} aparece {quantidade} Vez(es) no dataset.', file=saida)