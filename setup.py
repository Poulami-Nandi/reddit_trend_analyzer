from setuptools import setup, find_packages

setup(
    name='reddit_trend_analyzer',
    version='0.1.0',
    author='Poulami Nandi',
    author_email='nandi.poulami91@gmail.com',
    description='Reddit Hashtag/Keyword Trend Analyzer using PRAW, SQLite, and Streamlit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/reddit_trend_analyzer',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'praw',
        'textblob',
        'pandas',
        'matplotlib',
        'seaborn',
        'streamlit'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
