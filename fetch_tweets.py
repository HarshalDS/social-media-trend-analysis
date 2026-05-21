import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "AI since:2025-01-01 until:2025-12-31"

tweets = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > 100:
        break

    tweets.append([
        tweet.date,
        tweet.user.username,
        tweet.content
    ])

df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet"])

print(df.head())

df.to_csv("api_data/live_tweets.csv", index=False)

print("Tweets saved successfully!")