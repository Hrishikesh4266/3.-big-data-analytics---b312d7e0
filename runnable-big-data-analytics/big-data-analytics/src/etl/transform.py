def transform_data(df):
    return df.withColumnRenamed("value", "amount")
