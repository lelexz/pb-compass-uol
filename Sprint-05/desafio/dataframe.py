import boto3
import pandas as pd
from io import StringIO

#carregar o arquivo do S3
s3_client = boto3.client('s3')

#nome do bucket e do arquivo
bucket = 'bucket-desafio5'
arquivo = 'acidentes-transito.csv'

#baixando o arquivo do S3
csv_obj = s3_client.get_object(Bucket=bucket, Key=arquivo)
body = csv_obj['Body']
csv_string = body.read().decode('ISO-8859-1')

#lendo o arquivo .csv
df = pd.read_csv(StringIO(csv_string), encoding='ISO-8859-1', delimiter=';')

#removendo espaços
df.columns = df.columns.str.strip()

#utilizando duas funções de agregação
total_acidentes = pd.DataFrame({ 'total_acidentes': [df['Nº_boletim'].count()]})
media_idade = pd.DataFrame({'media_idade': [round(df['Idade'].mean())]})

#função condicional
df['maior_idade'] = df['Idade'].apply(lambda x: 'SIM' if x >=18 else 'Não informado' if x == 0 else 'NÃO')

#função de conversão
df['data_hora_boletim'] = pd.to_datetime(df['data_hora_boletim'], format='%d/%m/%Y %H:%M')

#função de data
df['ano'] = df['data_hora_boletim'].dt.year

#função de string
df['pedestre'] = df['pedestre'].str.replace('S', 'SIM')

#filtrando dados usando operadores lógicos
filtro = df[(df.cinto_seguranca.str.strip() == 'NÃO') & 
            ((df.desc_severidade.str.strip() == 'FATAL') & 
             (df.condutor.str.strip() == "S"))]


#salvando os dataframes em um arquivo csv
filtro.to_csv('df_filtrado.csv', index=False)
total_acidentes.to_csv('total_acidentes.csv', index=False)
media_idade.to_csv('media_idade.csv', index=False)

#nome do csv no bucket
df_filtrado_nome = 'df_filtrado.csv'
total_acidentes_nome = 'total_acidentes.csv'
media_idade_nome = 'media_idade.csv'

#fazendo uploado do csv para o bucket
s3_resource = boto3.resource('s3')
s3_resource.Bucket(bucket).upload_file('df_filtrado.csv', df_filtrado_nome)
s3_resource.Bucket(bucket).upload_file('total_acidentes.csv', total_acidentes_nome)
s3_resource.Bucket(bucket).upload_file('media_idade.csv', media_idade_nome)

print(f'Arquivos enviados para o bucket com sucesso.')