import time
import random
from textblob import TextBlob

# Sample Streaming News
sample_news = [
    "AI is transforming healthcare rapidly",
    "Tech layoffs continue across companies",
    "New startup raises funding successfully",
    "Cybersecurity threats increasing globally",
    "Cloud computing demand grows strongly",
    "Economic uncertainty impacts tech market",
    "Breakthrough in robotics innovation",
    "Data privacy concerns rising worldwide"
]

print("Starting Real-Time Streaming Analytics...\n")

for i in range(20):

    news = random.choice(sample_news)

    sentiment_score = TextBlob(news).sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Incoming News {i+1}:")
    print(f"Title: {news}")
    print(f"Sentiment Score: {sentiment_score}")
    print(f"Detected Sentiment: {sentiment}")

    print("-" * 60)

    time.sleep(2)

print("Streaming Analytics Completed!")