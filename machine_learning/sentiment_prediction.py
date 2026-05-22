import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("api_data/live_news.csv")

# Features and Labels
X = df["Title"]
y = df["Sentiment"]

# Convert Text into Numerical Features
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = MultinomialNB()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")

# Classification Report
print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# Test Custom Predictions
custom_news = [
    "AI startup receives huge investment",
    "Massive layoffs hit tech companies",
    "New innovation boosts cloud computing"
]

custom_vectorized = vectorizer.transform(custom_news)

predictions = model.predict(custom_vectorized)

print("\nCustom News Predictions:\n")

for news, prediction in zip(custom_news, predictions):

    print(f"News: {news}")
    print(f"Predicted Sentiment: {prediction}")

    print("-" * 50)