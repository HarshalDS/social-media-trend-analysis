import re
import pandas as pd
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_tweet(tweet):

    tweet = re.sub(r'http\S+', '', tweet)

    tweet = re.sub(r'@\w+', '', tweet)

    tweet = re.sub(r'[^a-zA-Z\s]', '', tweet)

    tweet = tweet.lower()

    tweet_words = tweet.split()

    filtered_words = [
        word for word in tweet_words
        if word not in stop_words
    ]

    return " ".join(filtered_words)