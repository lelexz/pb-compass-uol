with open('actors.csv', 'r', encoding='latin-1') as arquivo:
    with open('etapa2.txt', 'w', encoding='utf-8') as saida:
      bilheteria_total = 0
      contador = 0
      
      next(arquivo)
      for linha in arquivo:
          if '"Robert Downey, Jr."' in linha: 
              linha = linha.replace('"Robert Downey, Jr."', 'Robert Downey Jr.')
          dados = linha.strip().split(',')
          gross = float(dados[5])
          bilheteria_total += gross
          contador += 1
      media = bilheteria_total / contador 
      print(f'A média de bilheteria bruta é: {media:.2f}.', file=saida)              
    