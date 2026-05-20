import pandas as pd

from src.data_cleaning import clean_tweet
from src.sentiment_analysis import get_sentiment
from src.visualization import (
    plot_sentiment_distribution,
    plot_polarity_histogram
)

from textblob import TextBlob

df = pd.read_csv(
    "training.csv",
    encoding='latin-1',
    nrows=5000
)

df.columns = [
    'sentiment',
    'id',
    'date',
    'query',
    'user',
    'tweet'
]

df = df[['sentiment', 'tweet']]

df['clean_tweet'] = df['tweet'].apply(clean_tweet)

df['polarity'] = df['clean_tweet'].apply(
    lambda x: TextBlob(x).sentiment.polarity
)

df['sentiment_label'] = df['clean_tweet'].apply(get_sentiment)

print(df.head())

plot_sentiment_distribution(df)

plot_polarity_histogram(df)