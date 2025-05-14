import praw
import sqlite3
from textblob import TextBlob
from datetime import datetime

def main():
    # Setup Reddit API (replace with your credentials)
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='YOUR_USER_AGENT')

    # Connect to SQLite database
    conn = sqlite3.connect('data/reddit_trends.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT,
        title TEXT,
        score INTEGER,
        url TEXT,
        created_utc TEXT,
        sentiment REAL
    )
    ''')
    conn.commit()

    # Define keywords
    keywords = ['AI', 'ChatGPT', 'Python', 'Quantum Computing']

    # Collect posts from subreddit
    subreddit = reddit.subreddit('technology')
    for submission in subreddit.new(limit=100):
        for keyword in keywords:
            if keyword.lower() in submission.title.lower():
                sentiment = TextBlob(submission.title).sentiment.polarity
                cursor.execute('''
                    INSERT INTO posts (keyword, title, score, url, created_utc, sentiment)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    keyword,
                    submission.title,
                    submission.score,
                    submission.url,
                    datetime.utcfromtimestamp(submission.created_utc).isoformat(),
                    sentiment
                ))
                print(f"Stored post: {submission.title}")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
