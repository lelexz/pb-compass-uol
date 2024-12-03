import requests 
import pandas as pd
import chave_api
from IPython.display import display

#chave da API
api_key = chave_api.chave

#URL da API
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

#fazendo requisição à API
response = requests.get(url)

#convertendo a resposta para JSON
data = response.json()

#criando uma lista para armazenar os filmes
filmes = []

#passando por cada filme e criando um dicionário com as informações de cada um 
for movie in data['results']:
    df = {
        'Título': movie['title'],
        'Data de lançamento': movie['release_date'],
        'Visão geral': movie['overview'],
        'Votos': movie['vote_count'],
        'Média de votos': movie['vote_average']
    }

    #colocando cada filme na lista
    filmes.append(df)

#criando um dataframe com os dados
df = pd.DataFrame(filmes)

#exibindo o dataframe
display(df)