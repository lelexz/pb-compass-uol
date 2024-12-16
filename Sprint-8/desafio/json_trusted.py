import sys
from datetime import datetime
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, ArrayType
from pyspark.sql.functions import col, when

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

current_date = datetime.now().strftime("%Y/%m/%d")

input_path = "s3://bkt-desafio/Raw/tmdb/json/2024/12/02/*"
output_path = f"s3://bkt-desafio/Trusted/JSON/{current_date}"

schema = StructType([
    StructField("imdb_id", StringType(), True),
    StructField("director", StringType(), True),
    StructField("budget", FloatType(), True),
    StructField("revenue", FloatType(), True),
    StructField("popularity", FloatType(), True),
    StructField("vote_average", FloatType(), True),
    StructField("original_language", StringType(), True),
    StructField("production_countries", ArrayType(StringType()), True),
])

tmdb_df = spark.read.schema(schema).json(input_path)

tmdb_df = tmdb_df.withColumn("production_countries", col("production_countries").getItem(0))

tmdb_df = tmdb_df.withColumn("budget", when(col("budget") == 0, None).otherwise(col("budget")))
tmdb_df = tmdb_df.withColumn("revenue", when(col("revenue") == 0, None).otherwise(col("revenue")))

tmdb_df = tmdb_df.withColumn("budget", col("budget").cast(IntegerType())) 
tmdb_df = tmdb_df.withColumn("revenue", col("revenue").cast(IntegerType()))

tmdb_df.write.parquet(output_path, mode="overwrite")

job.commit()