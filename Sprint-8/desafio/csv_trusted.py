import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.sql.functions import split, col


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

movies_df = spark.read.csv("s3://bkt-desafio/Raw/Local/CSV/Movies/2024/11/05/movies.csv", header=True, inferSchema=True, sep="|")

movies_filtered = movies_df.filter(col("genero").contains("Crime"))

movies_filtered = movies_filtered.withColumnRenamed("tituloPincipal", "tituloPrincipal")

movies_filtered = movies_filtered.dropDuplicates(["id", "tituloPrincipal", "anoLancamento"])

movies_filtered.write.parquet("s3://bkt-desafio/Trusted/CSV/", mode="overwrite")

job.commit() 