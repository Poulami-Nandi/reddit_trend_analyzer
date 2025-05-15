from reddit_trend_analyzer import collect_data, analyze_data, query_data

import argparse

def main():
    parser = argparse.ArgumentParser(description='Reddit Hashtag/Keyword Trend Analyzer CLI')
    parser.add_argument('--collect', action='store_true', help='Collect Reddit posts and store in SQLite database')
    parser.add_argument('--analyze', action='store_true', help='Analyze and visualize stored Reddit data')
    parser.add_argument('--query', action='store_true', help='Run predefined SQL queries on the dataset')

    args = parser.parse_args()

    if args.collect:
        print("\n🚀 Starting data collection...")
        collect_data.main()
        print("\n✅ Data collection completed.")

    if args.analyze:
        print("\n📊 Starting data analysis & visualization...")
        analyze_data.main()
        print("\n✅ Data analysis completed.")

    if args.query:
        print("\n🔎 Running SQL queries...")
        query_data.main()
        print("\n✅ Querying completed.")

    if not (args.collect or args.analyze or args.query):
        print("\n⚠ Please provide at least one command. Use --help to see available options.")

if __name__ == '__main__':
    main()
