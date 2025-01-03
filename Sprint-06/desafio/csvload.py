import boto3
from datetime import datetime
import chaves_aws

#configurando chaves de acesso e região
session = boto3.Session(
    aws_access_key_id=chaves_aws.aws_access_key_id,
    aws_secret_access_key=chaves_aws.aws_secret_access_key,
    aws_session_token=chaves_aws.aws_session_token,
    region_name="us-east-1",
)
    
#criando cliente s3
s3 = session.client("s3")

#nome do bucket
bucket = chaves_aws.bucket

#criando bucket
s3.create_bucket(Bucket=bucket)

#lendo arquivos csv
def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, "r") as file:
        data = file.read()
    print(f"Arquivo {caminho_arquivo} lido.")
    return data


def carregar_no_s3(data, bucket, arquivo):
    
    #padronizando a gravação dos dados no s3
    data_atual = datetime.now()
    ano = data_atual.strftime("%Y")
    mes = data_atual.strftime("%m")
    dia = data_atual.strftime("%d")
    s3_key = f"Raw/Local/CSV/{arquivo}/{ano}/{mes}/{dia}/{arquivo.lower()}.csv"

    #colocando objetos no bucket
    s3.put_object(Body=data, Bucket=bucket, Key=s3_key)
    print(f"Dados do arquivo {arquivo.lower()}.csv enviados para S3 com sucesso.")

#lendo arquivos csv
movies = ler_csv("movies.csv")
series = ler_csv("series.csv")

#carregando dados para o S3
carregar_no_s3(movies, bucket, "Movies")
carregar_no_s3(series, bucket, "Series")

