import boto3

#criando um cliente S3
s3 = boto3.client('s3')

#nome do bucket
bucket = 'bucket-desafio5'

#crinado o bucket
s3.create_bucket(Bucket=bucket)

#caminho do csv
arquivo = r'c:\Users\Windows\Downloads\desafio\si_env-2021.csv'

#nome do csv no bucket
arquivo_nome = 'acidentes-transito.csv'

#fazendo upload do arquivo para o bucket
s3_resource = boto3.resource('s3')
s3_resource.Bucket(bucket).upload_file(arquivo, arquivo_nome)

print(f'Arquivo {arquivo_nome} enviado para o bucket {bucket} com sucesso.')
