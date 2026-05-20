import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):

    sentiment_counts = df['sentiment_label'].value_counts()

    plt.figure(figsize=(6,6))

    plt.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct='%1.1f%%'
    )

    plt.title("Sentiment Distribution")

    plt.show()


def plot_polarity_histogram(df):

    plt.figure(figsize=(8,5))

    plt.hist(df['polarity'], bins=30)

    plt.xlabel("Polarity")

    plt.ylabel("Count")

    plt.title("Sentiment Polarity Distribution")

    plt.show()