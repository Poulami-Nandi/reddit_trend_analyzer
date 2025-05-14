import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Initialize Streamlit page
st.set_page_config(page_title="Reddit Hashtag/Keyword Trend Analyzer", layout="wide")

# Custom app title and intro
st.title("📊 Reddit Hashtag/Keyword Trend Analyzer (Streamlit Dashboard)")
st.markdown("""
This app allows you to:
- Analyze Reddit posts containing specific keywords.
- Explore keyword frequency, sentiment trends, and popular posts.
- Visualize insights interactively.

Data is collected and stored in **SQLite database (`reddit_trends.db`)**.
""")

# Load data
@st.cache_data
def load_data():
    conn = sqlite3.connect('data/reddit_trends.db')
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    conn.close()
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    df['date'] = df['created_utc'].dt.date
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔎 Filters")
keywords = df['keyword'].unique().tolist()
selected_keywords = st.sidebar.multiselect("Select Keywords", keywords, default=keywords)

# Filter data
filtered_df = df[df['keyword'].isin(selected_keywords)]

st.write(f"### Total Posts Collected: {len(filtered_df)}")
st.write(f"### Keywords Analyzed: {', '.join(selected_keywords)}")

# 📅 Keyword Frequency Over Time
st.subheader("📅 Keyword Frequency Over Time")
freq = filtered_df.groupby(['date', 'keyword']).size().reset_index(name='counts')
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=freq, x='date', y='counts', hue='keyword', marker='o', ax=ax1)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# 😊 Sentiment Distribution
st.subheader("😊 Sentiment Distribution by Keyword")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.boxplot(data=filtered_df, x='keyword', y='sentiment', ax=ax2)
st.pyplot(fig2)

# 💡 Sentiment Trend Over Time
st.subheader("💡 Average Sentiment Over Time")
sentiment_trend = filtered_df.groupby(['date', 'keyword'])['sentiment'].mean().reset_index()
fig3, ax3 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=sentiment_trend, x='date', y='sentiment', hue='keyword', marker='o', ax=ax3)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

# 📊 Keyword Popularity Pie Chart
st.subheader("📊 Keyword Popularity Distribution")
fig4, ax4 = plt.subplots(figsize=(8, 6))
filtered_df['keyword'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, ax=ax4)
plt.axis('equal')
st.pyplot(fig4)

# ☁️ Word Cloud
st.subheader("☁️ Word Cloud of Post Titles")
text = ' '.join(filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=set(STOPWORDS)).generate(text)
fig5, ax5 = plt.subplots(figsize=(15, 7))
ax5.imshow(wordcloud, interpolation='bilinear')
ax5.axis('off')
st.pyplot(fig5)

# 🔝 Top Posts Table
st.subheader("🔝 Top 10 Most Upvoted Posts")
top_posts = filtered_df.sort_values('score', ascending=False).head(10)
st.dataframe(top_posts[['keyword', 'title', 'score', 'url', 'created_utc']])

# 🔥 Sentiment Heatmap
st.subheader("🔥 Sentiment Heatmap (Avg Sentiment per Day)")
pivot = filtered_df.pivot_table(values='sentiment', index='date', columns='keyword', aggfunc='mean')
fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt=".2f", ax=ax6)
st.pyplot(fig6)
