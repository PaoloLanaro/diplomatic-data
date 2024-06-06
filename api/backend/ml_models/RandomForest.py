import pandas as pd
import numpy as np
from backend.db_connection import db
import logging
import os
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from collections import Counter
from textblob import TextBlob
from sklearn.ensemble import RandomForestClassifier

logger = logging.getLogger()

def train(news_data):
    """
    Description: Training the model and then I believe storing it in SQL somewhere instead of just importing it as a csv? idk though 

    Args: 
        text(string): text used to find the sentiment score and word count
        queried(string): the country of interest that the article is related to

    Returns:
        source_country (string): the country that the model believes it came from
    """

    # rn the data is just in as like the big main csv that we're using, come back to this late bc i know this isn't right

    # DATA ClEANING JAZZ
    # drop the columns im not using
    news_data.drop(['Unnamed: 0', 'date', 'text', 'url', 'Safety Index', 'source_country', 'month', 'hour_of_day', 'source_to_queried_count'], axis=1, inplace=True)
    news_data.dropna(axis=0, inplace=True)

    # one hot encoding
    news_data = pd.get_dummies(news_data, columns=['queried_country'], drop_first=True)
    news_data
    
    # X and y
    X = news_data.drop(columns=['source_country']) 
    y = news_data['source_country']

    # splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # implement the random forest regressor
    rf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

    # fit the model
    classifier = rf.fit(X_train, y_train)

    return classifier # this is a numpy array. idk if thats the form that is needed


def predict_rf(text, queried):
    """
    Description: Using the sentiment score, word count, and queried country, predicting the source country using 

    Args: 
        text(string): text used to find the sentiment score and word count
        queried(string): the country of interest that the article is related to

    Returns:
        source_country (string): the country that the model believes it came from
    """

    # finding word count
    words = text.split()
    count = len(words)
    
    # sentiment
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    cursor = db.get_db().cursor()

    predictions = rf.predict(X)

    return np.dot(add_bias_column(X), m)