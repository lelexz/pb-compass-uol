##   Sprint 3 - Desafio 

### Objetivo
O objetivo desse desafio foi ler um arquivo .csv, processar seus dados e gerar informações e gráficos utilizando as bibliotecas Pandas e Matplotlib.


### 1. Leitura e remoção de duplicatas
<p> Para ler o arquivo, utilizei a função read_csv da biblioteca Pandas. Como parâmetros, especifiquei o nome do arquivo .csv e o separador, que nesse caso era a vírgula.

Para remover duplicatas, apliquei a função drop_duplicates com o parâmetro keep='first', garantindo que apenas o primeiro registro fosse mantido.  </p>

### 2. Tratamento de dados e criação de gráficos
<p>Nem todas as colunas do dataset estavam com o formato ideal. Por isso, para gerar a maioria dos gráficos, precisei primeiro converter as colunas em strings e, depois, transformá-las em inteiros.

Para criar os gráficos, utilizei a biblioteca Matplotlib, combinada com a Pandas, para facilitar a manipulação dos dados e a personalização dos gráficos.
</p>