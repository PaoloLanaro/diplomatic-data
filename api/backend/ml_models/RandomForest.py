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

def clean(news_data):
    """cleans the data and extracts the X and y values that will be used for the model
    
    Args:
        news_data (df): can be either 1-d or 2-d array containing information regarding the training X values
        
    
    Returns:
        X (array): can be either 1-d or 2-d array containing information regarding the training X values
        y (array): a 1-d array whcich includes all corresponding response values to X
    """

    # drop the columns im not using
    news_data.drop(['Unnamed: 0', 'date', 'url', 'Safety Index'], axis=1, inplace=True)
    news_data.dropna(axis=0, inplace=True)

    # adding word count
    news_data['word_count'] = news_data['text'].apply(lambda x: len(x.split()))

    # drop the columns im not using
    news_data.drop(['text'], axis=1, inplace=True)
    news_data.dropna(axis=0, inplace=True)

    # one hot encoding
    news_data = pd.get_dummies(news_data, columns=['queried_country'], drop_first=True)

    # X and y
    X = news_data.drop(columns=['source_country']) 
    y = news_data['source_country']

    return X, y

def train(news_data):
    """
    Description: Training the model agh 

    Args: 
        text(string): text used to find the sentiment score and word count
        queried(string): the country of interest that the article is related to

    Returns:
        source_country (string): the country that the model believes it came from
    """

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # implement the random forest regressor
    rf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

    # fit the model
    rf.fit(X_train, y_train)

    # fit the model
    classifier = rf.fit(X_train, y_train)

    return classifier 


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

    prediction = rf.predict(X)

    return prediction