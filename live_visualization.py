import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("api_data/live_news.csv")

# Sentiment Count Plot
sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind="bar")

plt.title("Live News Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.savefig("api_data/live_sentiment_bar_chart.png")
plt.show()

# Polarity Histogram
plt.figure(figsize=(8, 5))

plt.hist(df["Polarity"], bins=20)

plt.title("Live News Polarity Distribution")
plt.xlabel("Polarity Score")
plt.ylabel("Frequency")

plt.savefig("api_data/live_polarity_histogram.png")
plt.show()