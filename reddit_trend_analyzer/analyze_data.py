import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('data/reddit_trends.db')

    # Load data
    df = pd.read_sql_query("SELECT * FROM posts", conn)
    conn.close()

    # Convert timestamps
    df['created_utc'] = pd.to_datetime(df['created_utc'])
    df['date'] = df['created_utc'].dt.date

    # Keyword frequency over time
    freq = df.groupby(['date', 'keyword']).size().reset_index(name='counts')

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=freq, x='date', y='counts', hue='keyword', marker='o')
    plt.title('Keyword Frequency Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Sentiment distribution
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='keyword', y='sentiment')
    plt.title('Sentiment Distribution by Keyword')
    plt.show()

if __name__ == '__main__':
    main()
