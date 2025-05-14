import streamlit as st

# 🎨 Welcome & App Description
st.title("📊 Reddit Hashtag/Keyword Trend Analyzer")
st.markdown("""
Welcome to the **Reddit Hashtag/Keyword Trend Analyzer**!  
This app allows you to:
- Collect and analyze Reddit posts containing specific keywords.
- Track **keyword frequency trends over time**.
- Analyze **sentiment distribution by keyword**.
- Explore the **top most upvoted posts** for your selected keywords.

---

### 📋 How to Use
1. Use the **sidebar filters** to select the keywords you want to analyze.
2. View the **line chart** for frequency trends.
3. Explore **sentiment analysis** via box plots.
4. Scroll down to see the **top posts table** with direct links to Reddit.

---

🔗 Powered by:
- [Reddit API (PRAW)](https://praw.readthedocs.io/en/latest/)
- [SQLite](https://www.sqlite.org/index.html)
- [TextBlob Sentiment Analysis](https://textblob.readthedocs.io/en/dev/)
- [Streamlit](https://streamlit.io)

""")
