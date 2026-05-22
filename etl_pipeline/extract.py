import pandas as pd
from newsapi import NewsApiClient
from textblob import TextBlob

# API Key
API_KEY = "a741f68ae2de43faa496885eb73d98e9"

# Initialize News API
newsapi = NewsApiClient(api_key=API_KEY)

def extract_news_data():

    # Fetch News
    articles = newsapi.get_everything(
        q="technology OR AI OR startups",
        language="en",
        sort_by="publishedAt",
        page_size=20
    )

    processed_data = []

    for article in articles["articles"]:

        title = article["title"]

        if title:

            sentiment = TextBlob(title).sentiment

            processed_data.append({
                "Title": title,
                "Source": article["source"]["name"],
                "Published_Date": article["publishedAt"],
                "Polarity": sentiment.polarity,
                "Sentiment": (
                    "Positive"
                    if sentiment.polarity > 0
                    else "Negative"
                    if sentiment.polarity < 0
                    else "Neutral"
                )
            })

    # Convert to DataFrame
    df = pd.DataFrame(processed_data)

    print("Extraction Completed Successfully!")

    return df