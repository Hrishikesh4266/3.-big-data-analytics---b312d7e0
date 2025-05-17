from pyspark.sql import SparkSession
from src.etl.data_ingest import load_data
from src.etl.clean_data import clean_data
from src.etl.transform import transform_data

def run_spark_job(input_path):
    spark = SparkSession.builder.appName("BigDataAnalytics").getOrCreate()

    df = load_data(spark, input_path)
    df_clean = clean_data(df)
    df_transformed = transform_data(df_clean)

    df_transformed.show()
    spark.stop()
