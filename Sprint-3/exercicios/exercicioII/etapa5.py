with open('actors.csv', 'r', encoding='latin-1') as arquivo:
    with open('etapa5.txt', 'w', encoding='utf-8') as saida:
        next(arquivo)
        
        receita_atores = {}
        
        for linha in arquivo:
            if '"Robert Downey, Jr."' in linha: 
              linha = linha.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
            dados = linha.strip().split(',')
            
            ator = dados[0]  
            receita_bruta = dados[1]
            
            if ator in receita_atores:
                receita_atores[ator] += receita_bruta
            else:
                receita_atores[ator] = receita_bruta
                
        atores_ordenados = sorted(receita_atores.items(), key=lambda x: x[1], reverse=True)
        
        for ator, receita in atores_ordenados:
            print(f'{ator} - {receita}', file=saida)