##   Sprint 5 - Desafio 

### Objetivo
O objetivo desse desafio foi criar um bucket no S3 utilizando o boto3 e carregar um conjunto de dados nele.


### Conjunto de dados
O conjunto de dados escolhido foi "Relação das pessoas envolvidas nos acidentes de trânsito com vítima" em 2021, elaborado pela Prefeitura de Belo Horizonte. Ele inclui informações como: 

* Número de envolvidos no acidente
* Data e hora do registro do boletim 
* Descrição da severidade do acidente


### Criação do bucket
Primeiro, importei a biblioteca boto3 e criei um cliente S3 para poder interagir com o serviço. Defini o nome do bucket como 'bucket-desafio5' e criei ele com o comando create_bucket(). Depois, especifiquei o caminho do arquivo CSV local e o nome que ele teria dentro do bucket.

Para configurar a conexão entre o boto3 e o S3, utilizei a access key através do AWS CLI. Primeiro, instalei o AWS CLI no meu sistema e, em seguida, executei o comando aws configure. Depois, defini as variáveis de ambiente.

![Clique aqui](../evidencias/desafio/definindo_variaveis_ambiente.jpg)

Para enviar o arquivo, utilizei o recurso upload_file() da biblioteca boto3, que faz o upload direto do arquivo para o bucket. No final, o arquivo foi enviado com sucesso e a mensagem de confirmação foi exibida no terminal.

![Clique aqui](../evidencias/desafio/enviando_bucket.jpg)


### Criação do dataframe
Para criar os dataframes, comecei importando as bibliotecas necessárias, incluindo o boto3 para interagir com o S3 e o pandas para manipular os dados.  Também importei o StringIO da biblioteca io, que me ajudou a ler o conteúdo do arquivo CSV que baixei do S3. O StringIO é útil porque transforma a string que contém os dados do CSV em algo que o pandas pode ler como um arquivo.

Em seguida, criei um cliente S3 com o comando boto3.client('s3') e defini o nome do bucket e do arquivo CSV que queria baixar. Usei o método get_object() para pegar o arquivo do S3 e obtive seu conteúdo. Depois, decodei esse conteúdo usando a codificação ISO-8859-1.

![Clique aqui](../evidencias/desafio/bucket_e_arquivo.jpg)

Com o conteúdo do CSV em uma string, utilizei o StringIO para criar um objeto que o pandas pudesse ler. Isso me permitiu usar a função pd.read_csv() para ler e transformar os dados em um dataframe.

![Clique aqui](../evidencias/desafio/lendo_csv.jpg)

Depois, fiz algumas transformações e limpeza nos dados, removendo espaços nos nomes das colunas e utilizando algumas funções para obter informações. Com os dados prontos, criei três dataframes diferentes.

![Clique aqui](../evidencias/desafio/tres_dataframes.jpg)

Por fim, subi esses arquivos de volta para o bucket no S3 usando o método upload_file() da biblioteca boto3. Após a conclusão do upload, uma mensagem foi exibida no terminal confirmando que tudo tinha sido enviado com sucesso.

![Clique aqui](../evidencias/desafio/enviando_dataframes.jpg)


