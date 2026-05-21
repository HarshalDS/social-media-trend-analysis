from textblob import TextBlob
import requests
import pandas as pd

API_KEY = "a741f68ae2de43faa496885eb73d98e9"

url = f"https://newsapi.org/v2/everything?q=technology&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

articles = data["articles"]

news_data = []

def get_sentiment_label(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

for article in articles:
    sentiment = TextBlob(article["title"]).sentiment.polarity

    label = get_sentiment_label(sentiment)

    news_data.append([
        article["title"],
        article["source"]["name"],
        article["publishedAt"],
        sentiment,
        label
    ])

df = pd.DataFrame(
    news_data,
    columns=["Title", "Source", "Published Date", "Polarity", "Sentiment"]
)

print(df.head())

df.to_csv("api_data/live_news.csv", index=False)

print("News data saved successfully!")