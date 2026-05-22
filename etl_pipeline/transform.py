from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def transform_news_data(input_df):

    # Start Spark Session
    spark = SparkSession.builder \
        .appName("ETL Transformation") \
        .getOrCreate()

    # Convert Pandas DF to Spark DF
    spark_df = spark.createDataFrame(input_df)

    # Enhanced Sentiment Categories
    transformed_df = spark_df.withColumn(
        "Sentiment_Score_Category",
        when(col("Polarity") > 0.5, "Highly Positive")
        .when(col("Polarity") > 0, "Positive")
        .when(col("Polarity") < -0.5, "Highly Negative")
        .when(col("Polarity") < 0, "Negative")
        .otherwise("Neutral")
    )

    print("Transformation Completed Successfully!")

    return transformed_df