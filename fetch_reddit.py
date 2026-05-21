import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="sentiment_analysis_project"
)

subreddit = reddit.subreddit("technology")

posts = []

for post in subreddit.hot(limit=100):
    posts.append([
        post.title,
        post.score,
        post.url
    ])

df = pd.DataFrame(posts, columns=["Title", "Score", "URL"])

print(df.head())

df.to_csv("api_data/reddit_posts.csv", index=False)

print("Reddit posts saved successfully!")