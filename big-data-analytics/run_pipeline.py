import os
from src.analytics.spark_jobs import run_spark_job

if __name__ == "__main__":
    input_path = "data/sample_data.csv"
    if os.path.exists(input_path):
        run_spark_job(input_path)
    else:
        print("Input file not found.")
