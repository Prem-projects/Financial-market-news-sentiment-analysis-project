# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVTWpefbajAagzHb15mKtiiAuFrRFklH

**Title of project: Financial Market News-Sentiment Analysis**

**Objective: Classifying financial text or news into positive,negative or neutral sentiments which directly gives the idea of bullish or bearish view of financial market.**

**Data source: YBI Foundation Github**

This is data of financial market top 25 news for the day and task is to train and predict del for overall sentiment analysis.

Import Library
"""

import pandas as pd

import numpy as np

"""Import Dataset"""

df=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Financial%20Market%20News.csv')

df.head()

df.info()

df.shape

df.columns

"""Get feature Selection"""

''.join(str(x) for x in df.iloc[1,2:27])

df.index

len(df.index)

news=[]
for row in range(0,len(df.index)):
  news.append(''.join(str(x) for x in df.iloc[row,2:27]))

type(news)

news[0]

X=news

type(X)

"""Get feature text conversion to bag of words"""

from sklearn.feature_extraction.text import CountVectorizer

cv=CounterVectorizer(lowercase=True,ngram_range=(1,1))

X=cv.fit_transform(X)

X.shape

y=df['Label']

y.shape

"""Get train test split"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,stratify=y,random_state=2529)

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier(n_estimators=200)

rf.fit(X_train,y_train)

y_pred=rf.predict(X_test)

from sklearn.metrices import classification_report,confusion_matrix,accuracy_score

confusion_matrix(y_test,y_pred)

print(classification_report(y_test,y_pred))

"""***EXPLANATION***:The project of financial market news-sentiment analysis is a data-driven approach that aims to analyze and gauge the sentiment of news articles, social media posts, and other textual data related to financial markets. The goal is to extract valuable insights from these textual sources and understand how public sentiment can impact financial markets.

Here's a general outline of the project:

Data Collection: The first step involves gathering relevant textual data from various sources, such as financial news websites, social media platforms (e.g., Twitter), financial forums, and press releases. This data could include headlines, articles, tweets, and comments related to specific financial assets, companies, or the overall market.

Preprocessing: Once the data is collected, it needs to be preprocessed to make it suitable for analysis. This step involves removing irrelevant information, converting text to lowercase, handling special characters, tokenization (splitting text into individual words or tokens), removing stopwords, and applying other text-cleaning techniques.

Sentiment Analysis: The core of the project is sentiment analysis, where machine learning algorithms or natural language processing (NLP) techniques are used to determine the sentiment of each text. Sentiment analysis categorizes the text as positive, negative, or neutral based on the sentiment expressed in the content.

Sentiment Scoring: After performing sentiment analysis on the textual data, the sentiment of each piece of news or social media post is quantified using a scoring system. This could involve assigning a numerical value to represent the sentiment, such as using a scale from -1 (negative sentiment) to 1 (positive sentiment).

Correlation with Financial Data: The sentiment scores obtained from the previous step are then correlated with financial market data, such as stock prices, trading volumes, or market indices. This analysis helps identify potential correlations between sentiment and market movements.

Visualizations and Insights: The project may use various data visualization techniques to present the results effectively. Visualizations could include sentiment trend charts, sentiment distribution plots, and correlation plots between sentiment and financial market data. The insights gained from this analysis can help traders, investors, and financial analysts make more informed decisions.

Sentiment-Based Strategies: Depending on the findings of the analysis, sentiment-based trading or investment strategies may be developed. For example, if a positive sentiment is strongly correlated with upward stock price movements, traders might use sentiment signals to inform their buy/sell decisions.

Model Improvement: The project can be an iterative process, where the sentiment analysis model is continually refined and improved based on feedback and new data. The model may be updated to handle domain-specific language, adapt to changing market conditions, and handle noise and misinformation in the data.

Overall, the financial market news-sentiment analysis project is an essential tool for understanding how public sentiment impacts financial markets and can provide valuable insights to market participants for better decision-making.
"""