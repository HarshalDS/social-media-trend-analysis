from pyspark.sql.functions import col, when

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Social Media Trend Analysis") \
    .getOrCreate()

# Load CSV File
df = spark.read.csv(
    "api_data/live_news.csv",
    header=True,
    inferSchema=True
)

# Show Dataset
print("Dataset Preview:")
df.show(5)

# Show Schema
print("Dataset Schema:")
df.printSchema()

# Sentiment Count Analysis
print("Sentiment Count:")
df.groupBy("Sentiment").count().show()

# Average Polarity
print("Average Polarity:")
df.selectExpr("avg(Polarity) as Average_Polarity").show()

# Create Sentiment Score Category
df = df.withColumn(
    "Sentiment_Score_Category",
    when(col("Polarity") > 0.5, "Highly Positive")
    .when(col("Polarity") > 0, "Positive")
    .when(col("Polarity") < -0.5, "Highly Negative")
    .when(col("Polarity") < 0, "Negative")
    .otherwise("Neutral")
)

print("Enhanced Sentiment Categories:")
df.select(
    "Title",
    "Polarity",
    "Sentiment_Score_Category"
).show(10, truncate=False)

# Category Count
print("Enhanced Category Count:")
df.groupBy("Sentiment_Score_Category").count().show()

# Filter Positive Trends
positive_df = df.filter(col("Sentiment_Score_Category").isin(
    "Positive",
    "Highly Positive"
))

print("Positive Trend News:")
positive_df.select(
    "Title",
    "Polarity",
    "Sentiment_Score_Category"
).show(10, truncate=False)

# Filter Negative Trends
negative_df = df.filter(col("Sentiment_Score_Category").isin(
    "Negative",
    "Highly Negative"
))

print("Negative Trend News:")
negative_df.select(
    "Title",
    "Polarity",
    "Sentiment_Score_Category"
).show(10, truncate=False)

# Top Positive Trends
print("Top Positive Trends:")

df.orderBy(col("Polarity").desc()).select(
    "Title",
    "Polarity"
).show(10, truncate=False)

# Top Negative Trends
print("Top Negative Trends:")

df.orderBy(col("Polarity").asc()).select(
    "Title",
    "Polarity"
).show(10, truncate=False)

spark.stop()
