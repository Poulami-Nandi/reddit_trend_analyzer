![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

# 📊 Reddit Hashtag/Keyword Trend Analyzer

Track Reddit post trends and sentiment for your favorite hashtags or keywords using **Python, SQLite, and Streamlit**.

> Interactive and lightweight Reddit trend analyzer that collects, stores, analyzes, and visualizes keyword trends and sentiment in Reddit posts.

---

## 🚀 Features
- Collect Reddit posts containing specific keywords using **PRAW (Reddit API Wrapper)**.
- Perform **sentiment analysis using TextBlob**.
- Store posts and metadata in a **file-based SQLite database (`.db`)**.
- Visualize:
  - Keyword frequency trends over time.
  - Sentiment distribution by keyword.
  - Top upvoted posts.

---

## 🔧 Tech Stack
- Python 3.8+
- SQLite (file-based)
- PRAW (Reddit API)
- TextBlob (Sentiment Analysis)
- Pandas, Matplotlib, Seaborn (Data Analysis & Visualization)
- Streamlit (Dashboard UI)

---

## 📁 Project Structure
```bash
reddit_trend_analyzer/
├── reddit_trend_analyzer/ # Python package
├── data/ # SQLite database and data files
├── notebooks/ # Jupyter notebooks
├── scripts/ # CLI scripts
├── app.py # Streamlit app
├── main.py # CLI entry point
├── requirements.txt
├── LICENSE
└── README.md
```
---

## ⚙ Installation

1. Clone the repository:
```bash
git clone https://github.com/Poulami-Nandi/reddit_trend_analyzer.git
cd reddit_trend_analyzer
```
Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Usage
### Collect data:
```bash
python main.py --collect
```
### Analyze data:
```bash
python main.py --analyze
```
### Run Streamlit Dashboard:
```bash
streamlit run app.py
```
### Query data:
```bash
python main.py --query
```
---
## 💡 Contributing
Contributions are welcome!
Please read CONTRIBUTING.md for guidelines.
---
## 📜 License
This project is licensed under the MIT License. See LICENSE for details.
---
## 🙌 Acknowledgements
- [Reddit API] (https://praw.readthedocs.io/en/stable/)
- [TextBlob] (https://textblob.readthedocs.io/en/dev/)
- [Streamlit] ([Streamlit](https://streamlit.io/))
