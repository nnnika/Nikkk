import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.types import TimestampType

# SparkSession可以用来创建DataFrame，执行SQL，缓存表，以及读取parquet文件。用builder创造实例
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

