import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Social Media Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATASETS
# ---------------------------------------------------

df = pd.read_csv("api_data/live_news.csv")

youtube_df = pd.read_csv(
    "api_data/youtube_comments.csv"
)

# ---------------------------------------------------
# MACHINE LEARNING MODEL
# ---------------------------------------------------

combined_text = pd.concat([
    df["Title"],
    youtube_df["Comment"]
])

combined_sentiment = pd.concat([
    df["Sentiment"],
    youtube_df["Sentiment"]
])

X = combined_text
y = combined_sentiment

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vectorized, y)

# ---------------------------------------------------
# DASHBOARD HEADER
# ---------------------------------------------------

st.markdown("""
#  AI-Powered Social Media Intelligence Dashboard

### Real-Time Analytics • NLP • Machine Learning • PySpark • Databricks
""")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🎛 Dashboard Controls")

st.sidebar.markdown("""
### Project Features

- NLP Sentiment Analysis
- Machine Learning Prediction
- PySpark Analytics
- Databricks Integration
- YouTube Comment Analysis
- Real-Time API Data
- Interactive Dashboard
""")

selected_sentiment = st.sidebar.multiselect(
    "Select News Sentiment",
    options=df["Sentiment"].unique(),
    default=df["Sentiment"].unique()
)

filtered_df = df[
    df["Sentiment"].isin(selected_sentiment)
]

# ---------------------------------------------------
# KPI METRICS
# ---------------------------------------------------

positive_count = len(
    filtered_df[
        filtered_df["Sentiment"] == "Positive"
    ]
)

negative_count = len(
    filtered_df[
        filtered_df["Sentiment"] == "Negative"
    ]
)

neutral_count = len(
    filtered_df[
        filtered_df["Sentiment"] == "Neutral"
    ]
)

average_polarity = round(
    filtered_df["Polarity"].mean(),
    2
)

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "😊 Positive News",
    positive_count
)

col2.metric(
    "⚠️ Negative News",
    negative_count
)

col3.metric(
    "😐 Neutral News",
    neutral_count
)

col4.metric(
    "📈 Avg Polarity",
    average_polarity
)

st.divider()

# ---------------------------------------------------
# TABS
# ---------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    "📰 News Analysis",
    "🎥 YouTube Analysis",
    "🤖 ML Prediction"
])

# ===================================================
# NEWS ANALYSIS TAB
# ===================================================

with tab1:

    st.subheader("📄 Live News Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.subheader(
        "📈 News Sentiment Distribution"
    )

    sentiment_counts = (
        filtered_df["Sentiment"]
        .value_counts()
    )

    chart_col1, chart_col2 = st.columns(2)

    # -----------------------------------------------
    # BAR CHART
    # -----------------------------------------------

    with chart_col1:

        fig1, ax1 = plt.subplots()

        ax1.bar(
            sentiment_counts.index,
            sentiment_counts.values
        )

        ax1.set_title(
            "News Sentiment Bar Chart"
        )

        ax1.set_xlabel("Sentiment")

        ax1.set_ylabel("Count")

        st.pyplot(fig1)

    # -----------------------------------------------
    # PIE CHART
    # -----------------------------------------------

    with chart_col2:

        fig2, ax2 = plt.subplots()

        ax2.pie(
            sentiment_counts.values,
            labels=sentiment_counts.index,
            autopct='%1.1f%%'
        )

        ax2.set_title(
            "News Sentiment Pie Chart"
        )

        st.pyplot(fig2)

    st.divider()

    # -----------------------------------------------
    # TOP POSITIVE NEWS
    # -----------------------------------------------

    st.subheader(" Top Positive News")

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

    # -----------------------------------------------
    # TOP NEGATIVE NEWS
    # -----------------------------------------------

    st.subheader("Top Negative News")

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

# ===================================================
# YOUTUBE ANALYSIS TAB
# ===================================================

with tab2:

    st.subheader(
        "YouTube Comment Analysis"
    )

    st.dataframe(
        youtube_df,
        use_container_width=True
    )

    youtube_counts = (
        youtube_df["Sentiment"]
        .value_counts()
    )

    st.subheader(
        "YouTube Sentiment Distribution"
    )

    yt_col1, yt_col2 = st.columns(2)

    # -----------------------------------------------
    # YOUTUBE BAR CHART
    # -----------------------------------------------

    with yt_col1:

        fig3, ax3 = plt.subplots()

        ax3.bar(
            youtube_counts.index,
            youtube_counts.values
        )

        ax3.set_title(
            "YouTube Sentiment Bar Chart"
        )

        ax3.set_xlabel("Sentiment")

        ax3.set_ylabel("Count")

        st.pyplot(fig3)

    # -----------------------------------------------
    # YOUTUBE PIE CHART
    # -----------------------------------------------

    with yt_col2:

        fig4, ax4 = plt.subplots()

        ax4.pie(
            youtube_counts.values,
            labels=youtube_counts.index,
            autopct='%1.1f%%'
        )

        ax4.set_title(
            "YouTube Sentiment Pie Chart"
        )

        st.pyplot(fig4)

    st.divider()

    # -----------------------------------------------
    # POSITIVE COMMENTS
    # -----------------------------------------------

    st.subheader(
        "Top Positive Comments"
    )

    positive_comments = youtube_df[
        youtube_df["Sentiment"] == "Positive"
    ]

    st.dataframe(
        positive_comments.head(10),
        use_container_width=True
    )

    # -----------------------------------------------
    # NEGATIVE COMMENTS
    # -----------------------------------------------

    st.subheader(
        "Top Negative Comments"
    )

    negative_comments = youtube_df[
        youtube_df["Sentiment"] == "Negative"
    ]

    st.dataframe(
        negative_comments.head(10),
        use_container_width=True
    )

# ===================================================
# MACHINE LEARNING TAB
# ===================================================

with tab3:

    st.subheader(
        "🤖 AI Sentiment Prediction"
    )

    st.markdown("""
Enter custom news headlines, comments,
or social media text to predict sentiment.
""")

    user_input = st.text_area(
        "✍ Enter Custom Text"
    )

    if st.button("🚀 Predict Sentiment"):

        if user_input:

            input_vector = vectorizer.transform(
                [user_input]
            )

            prediction = model.predict(
                input_vector
            )[0]

            # ---------------------------------------
            # RESULT DISPLAY
            # ---------------------------------------

            if prediction == "Positive":

                st.success(
                    f"😊 Predicted Sentiment: {prediction}"
                )

            elif prediction == "Negative":

                st.error(
                    f"⚠️ Predicted Sentiment: {prediction}"
                )

            else:

                st.info(
                    f"😐 Predicted Sentiment: {prediction}"
                )

        else:

            st.warning(
                "Please enter text for prediction."
            )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "Built with Streamlit • NLP • Machine Learning • PySpark • Databricks"
)

st.success(
    "Dashboard Loaded Successfully!"
)