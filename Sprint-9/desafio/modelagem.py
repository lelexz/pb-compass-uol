import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, monotonically_increasing_id


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

csv_df = spark.read.parquet("s3://bkt-desafio/Trusted/CSV/*")
tmdb_df = spark.read.parquet("s3://bkt-desafio/Trusted/JSON/2024/12/11/*")

df = tmdb_df.join(csv_df, tmdb_df.imdb_id == csv_df.id, how="inner")
df = df.select(
    tmdb_df.imdb_id,
    csv_df.tituloPrincipal,
    csv_df.anoLancamento,
    csv_df.genero,
    csv_df.notaMedia,
    tmdb_df.director,
    tmdb_df.budget,
    tmdb_df.revenue,
    tmdb_df.popularity,
    tmdb_df.original_language,
    tmdb_df.production_countries
)

dim_filmes = df.select("tituloPrincipal", "genero", "director").withColumn("id_filme", monotonically_increasing_id())
dim_filmes = dim_filmes.select("id_filme", "tituloPrincipal", "genero", "director")
dim_filmes.write.mode("overwrite").parquet("s3://bkt-desafio/Refined/dim_filmes/")

dim_pais_producao = df.select("production_countries").distinct().withColumn("id_pais", monotonically_increasing_id())
dim_pais_producao = dim_pais_producao.select("id_pais", "production_countries")
dim_pais_producao.write.mode("overwrite").parquet("s3://bkt-desafio/Refined/dim_pais_producao/")

dim_tempo = df.select("anoLancamento").distinct().withColumn("id_ano", monotonically_increasing_id())
dim_tempo = dim_tempo.select("id_ano", "anoLancamento")
dim_tempo.write.mode("overwrite").parquet("s3://bkt-desafio/Refined/dim_tempo/")

df = df.join(dim_filmes, on=["tituloPrincipal", "genero", "director"], how="left")
df = df.join(dim_pais_producao, on=["production_countries"], how="left") 
df = df.join(dim_tempo, on=["anoLancamento"], how="left")

fatos = df.select(
    "imdb_id",
    "id_filme",
    "id_pais",
    "id_ano",
    "notaMedia",
    "budget",
    "revenue",
    "popularity"
)
fatos.write.mode("overwrite").parquet("s3://bkt-desafio/Refined/fatos/")



job.commit()