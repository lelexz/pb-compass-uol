import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions
from pyspark.sql import DataFrameWriter
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME] 
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#caminhos de entrada e saída no S3
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

#leitura do arquivo e dataframe
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [source_file]
    },
    "csv",
    {"withHeader": True, "separator": ","}
)


data_frame = df.toDF()
data_frame = data_frame.withColumn('total', data_frame['total'].cast('integer'))

#agrupando por ano e somando totais
df_group = data_frame.groupBy('ano').agg(functions.sum('total').alias('total'))
df_ordenado = df_group.orderBy('ano')

df_10 = df_ordenado.limit(10)
df_10.show()

df_10.write.mode('append').json(target_path)

job.commit()
