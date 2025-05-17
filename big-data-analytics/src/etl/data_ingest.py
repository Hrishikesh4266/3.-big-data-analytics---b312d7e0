from pyspark.sql import SparkSession

def load_data(spark, path):
    df = spark.read.csv(path, header=True, inferSchema=True)
    return df
