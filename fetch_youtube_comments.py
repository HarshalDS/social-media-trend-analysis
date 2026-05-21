from googleapiclient.discovery import build
from textblob import TextBlob
import pandas as pd

API_KEY = "AIzaSyCJnZn8hHvUAWtHXtsDHJuSpfx-mrP5vu8"

youtube = build('youtube', 'v3', developerKey=API_KEY)

video_id = "dQw4w9WgXcQ"   # Example video ID

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=100
)

response = request.execute()

comments_data = []

def get_sentiment_label(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

for item in response['items']:

    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

    polarity = TextBlob(comment).sentiment.polarity

    sentiment = get_sentiment_label(polarity)

    comments_data.append([
        comment,
        polarity,
        sentiment
    ])

df = pd.DataFrame(
    comments_data,
    columns=["Comment", "Polarity", "Sentiment"]
)

print(df.head())

df.to_csv("api_data/youtube_comments.csv", index=False)

print("YouTube comments saved successfully!")