import time
import random
import pandas as pd

# Sample Streaming Data
sample_news = [
    ["AI is transforming healthcare rapidly", "Positive"],
    ["Tech layoffs continue across companies", "Negative"],
    ["New startup raises funding successfully", "Positive"],
    ["Cybersecurity threats increasing globally", "Negative"],
    ["Cloud computing demand grows strongly", "Positive"],
    ["Economic uncertainty impacts tech market", "Negative"],
    ["Breakthrough in robotics innovation", "Positive"],
    ["Data privacy concerns rising worldwide", "Negative"]
]

print("Starting Real-Time Streaming Simulation...\n")

for i in range(20):

    news = random.choice(sample_news)

    streaming_record = {
        "Title": news[0],
        "Sentiment": news[1]
    }

    df = pd.DataFrame([streaming_record])

    print(f"Incoming Stream Data {i+1}:")
    print(df)
    print("-" * 50)

    time.sleep(2)

print("Streaming Simulation Completed!")