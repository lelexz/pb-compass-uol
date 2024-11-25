import boto3
import chave_api
import requests
from datetime import datetime
import chaves_aws
import json

#função de requisição à API
def fetch_tmdb_data(api_key, endpoint, params):
    #url da api com o endpoint específico
    url = f"https://api.themoviedb.org/3/{endpoint}"
    #adicionando a chave de API aos parâmetros
    params["api_key"] = api_key

    response = requests.get(url, params=params) #faz a requisição get

    if response.status_code == 200: #verifica se a resposta foi bem sucedida
        return response.json() #dados no formato json
    else:
        print(f"Falha: {response.status_code}") #se falhar, mostra o código do erro
        return None


def fetch_crime_movies(api_key, current_page=1):
    params = {
        "language": "pt-BR", #idioma de resposta
        "with_genres": 80,  #gênero de crime
        "page": current_page, #número da página
        "release_date.gte": "1990-01-01",  #filtrando a partir de 1990
        "release_date.lte": "2000-12-31",  #até 2000
    }
    return fetch_tmdb_data(api_key, "discover/movie", params)


def fetch_movie_details(api_key, movie_id):
    #buscando detalhes do filme
    details = fetch_tmdb_data(api_key, f"movie/{movie_id}", {})
    credits = fetch_tmdb_data(api_key, f"movie/{movie_id}/credits", {})

    if not details or not credits: #verifica se as requisições falharam
        return None

    return {
        "id": movie_id,
        "imdb_id": details.get("imdb_id", "Desconhecido"),
        "title": details.get("title"),
        "director": next(
        (person["name"] for person in credits["crew"] if person["job"] == "Director"),
        "Desconhecido"),  #extrai o nome do diretor da lista de créditos
        "duration": details.get("runtime", "Desconhecido"),
        "budget": details.get("budget", "Desconhecido"),
        "revenue": details.get("revenue", "Desconhecido"),
        "release_date": details.get("release_date", "Desconhecido"),
        "popularity": details.get("popularity", "Desconhecido"),
        "vote_average": details.get("vote_average", "Desconhecido"),  
        "original_language": details.get("original_language", "Desconhecido"),  
        "production_countries": [country["name"] for country in details.get("production_countries", [])] or "Desconhecido", #extrai os países de produção
    }

#função para buscar os filmes e salvar no S3
def lambda_handler(event, context):
    api_key = chave_api.chave
    bucket = "bkt-desafio"
    total_pages = 10 #número de páginas para buscar
    current_page = 1 #começando na primeira página
    tmdb_data = [] #lista para armazenar os dados dos filmes

    #loop para carregar todas as páginas
    while current_page <= total_pages:
        tmdb_response = fetch_crime_movies(api_key, current_page)

        if tmdb_response:
            print(f"Página {current_page} carregada com sucesso.")
            #itera cada filme que veio na resposta da api
            for movie in tmdb_response["results"]:
                #busca mais detalhes do filme utilizando o id
                movie_details = fetch_movie_details(api_key, movie["id"])
                #se encontrou os detalhes, joga na lista
                if movie_details:
                    tmdb_data.append(movie_details)

            if current_page >= total_pages:
                break  #sai do loop quando todas as páginas forem processadas

            current_page += 1
        else:
            print("Falha ao buscar dados da API.")
            break
    #dividindo os dados em grupos de 100 filmes
    group_data = [tmdb_data[i : i + 100] for i in range(0, len(tmdb_data), 100)]
    current_date = datetime.now().strftime("%Y/%m/%d")

    #envia os dados para o S3, um grupo de cada vez 
    for index, data_group in enumerate(group_data, start=1):
        upload_to_s3(json.dumps(data_group), bucket, f"tmdb_data_{index}", current_date)

#função para fazer upload dos dados no S3
def upload_to_s3(data, bucket, tipo, current_date):
    #caminho
    s3_key = f"Raw/tmdb/json/{current_date}/{tipo.lower()}.json"

    session = boto3.Session(
        aws_access_key_id=chaves_aws.access_key,
        aws_secret_access_key=chaves_aws.secret_key,
        aws_session_token=chaves_aws.session_token,
        region_name="us-east-1"
    )
    s3 = session.client("s3")

    s3.put_object(Body=data, Bucket=bucket, Key=s3_key)
    print(f"Dados carregados para S3: s3://{bucket}/{s3_key}")