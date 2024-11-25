import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import DataFrameWriter
from pyspark.sql import functions
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

df_n_feminino = data_frame.filter(data_frame.sexo == 'F')
df_n_feminino = df_n_feminino.withColumn('total', df_n_feminino['total'].cast('integer'))
df_maior = df_n_feminino.orderBy(functions.desc('total')).first()

df_maior_total = spark.createDataFrame([df_maior])

df_maior_total.write.mode('append').json(target_path)

job.commit()
