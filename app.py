import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Social Media Trend Analysis",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("api_data/live_news.csv")

# Dashboard Title
st.markdown("""
# 📊 Social Media Trend Analysis Dashboard

Real-Time Sentiment Analytics • NLP • Machine Learning • PySpark
""")

# Sidebar
st.sidebar.title("Dashboard Controls")

selected_sentiment = st.sidebar.multiselect(
    "Select Sentiment",
    options=df["Sentiment"].unique(),
    default=df["Sentiment"].unique()
)

filtered_df = df[df["Sentiment"].isin(selected_sentiment)]

# KPI Metrics
positive_count = len(
    filtered_df[filtered_df["Sentiment"] == "Positive"]
)

negative_count = len(
    filtered_df[filtered_df["Sentiment"] == "Negative"]
)

neutral_count = len(
    filtered_df[filtered_df["Sentiment"] == "Neutral"]
)

average_polarity = round(
    filtered_df["Polarity"].mean(),
    2
)

# Metric Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Positive News",
    positive_count
)

col2.metric(
    "Negative News",
    negative_count
)

col3.metric(
    "Neutral News",
    neutral_count
)

col4.metric(
    "Average Polarity",
    average_polarity
)

st.divider()

# Dataset Section
st.subheader("📄 Live News Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Charts Section
st.subheader("📈 Sentiment Distribution")

sentiment_counts = filtered_df["Sentiment"].value_counts()

chart_col1, chart_col2 = st.columns(2)

# Bar Chart
with chart_col1:

    fig1, ax1 = plt.subplots()

    ax1.bar(
        sentiment_counts.index,
        sentiment_counts.values
    )

    ax1.set_title("Bar Chart")

    st.pyplot(fig1)

# Pie Chart
with chart_col2:

    fig2, ax2 = plt.subplots()

    ax2.pie(
        sentiment_counts.values,
        labels=sentiment_counts.index,
        autopct='%1.1f%%'
    )

    ax2.set_title("Pie Chart")

    st.pyplot(fig2)

st.divider()

# Top Positive News
st.subheader("🚀 Top Positive News")

positive_news = filtered_df.sort_values(
    by="Polarity",
    ascending=False
)

st.dataframe(
    positive_news[
        ["Title", "Polarity", "Source"]
    ].head(10),
    use_container_width=True
)

# Top Negative News
st.subheader("⚠️ Top Negative News")

negative_news = filtered_df.sort_values(
    by="Polarity",
    ascending=True
)

st.dataframe(
    negative_news[
        ["Title", "Polarity", "Source"]
    ].head(10),
    use_container_width=True
)

st.success("Dashboard Loaded Successfully!")