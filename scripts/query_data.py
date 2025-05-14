import sqlite3
import pandas as pd

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('data/reddit_trends.db')

    # Top 10 most upvoted posts
    print("\n🔝 Top 10 Most Upvoted Posts:")
    df_top = pd.read_sql_query('''
        SELECT keyword, title, score, url, created_utc
        FROM posts
        ORDER BY score DESC
        LIMIT 10
    ''', conn)
    print(df_top)

    # Average sentiment per keyword
    print("\n😊 Average Sentiment per Keyword:")
    df_sentiment = pd.read_sql_query('''
        SELECT keyword, ROUND(AVG(sentiment), 3) as avg_sentiment, COUNT(*) as post_count
        FROM posts
        GROUP BY keyword
        ORDER BY avg_sentiment DESC
    ''', conn)
    print(df_sentiment)

    # Frequency by date
    print("\n📅 Keyword Frequency by Date:")
    df_freq = pd.read_sql_query('''
        SELECT DATE(created_utc) as date, keyword, COUNT(*) as post_count
        FROM posts
        GROUP BY DATE(created_utc), keyword
        ORDER BY date DESC, post_count DESC
    ''', conn)
    print(df_freq)

    conn.close()

if __name__ == '__main__':
    main()
