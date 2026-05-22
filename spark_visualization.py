from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import matplotlib.pyplot as plt

# Create Spark Session
spark = SparkSession.builder \
    .appName("Spark Visualization") \
    .getOrCreate()

# Load Dataset
df = spark.read.csv(
    "api_data/live_news.csv",
    header=True,
    inferSchema=True
)

# Convert Spark DataFrame to Pandas
pandas_df = df.toPandas()

# Sentiment Count Visualization
sentiment_counts = pandas_df["Sentiment"].value_counts()

plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind="bar")

plt.title("Spark Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.savefig("api_data/spark_sentiment_chart.png")

plt.show()

# Top Positive Trends
top_positive = pandas_df.sort_values(
    by="Polarity",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_positive["Title"],
    top_positive["Polarity"]
)

plt.title("Top Positive Trends")
plt.xlabel("Polarity Score")

plt.savefig("api_data/top_positive_trends.png")

plt.show()

spark.stop()