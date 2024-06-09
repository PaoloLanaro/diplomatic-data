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

    data = {
        'sentiment': [], 
        'word_count': [], 
        'country_written_from': []
    }

    for item in range(len(news_data) - 1):
        data['sentiment'].append(news_data[item]['sentiment'])
        data['country_written_about'].append(news_data[item]['country_written_about'])
        data['word_count'].append(len(news_data[item]['content'].split()))

    df = pd.DataFrame().from_dict(data)

    # one hot encoding
    news_data = pd.get_dummies(news_data, columns=['country_written_about'], drop_first=True)

    return df

def train_forest(news_data):
    """
    Description: Training the model agh 

    Args: 
        text(string): text used to find the sentiment score and word count
        queried(string): the country of interest that the article is related to

    Returns:
        source_country (string): the country that the model believes it came from
    """

    df = clean(news_data)

    y = df['country_written_about'].values
    X = df.drop(columns=['country_written_about'])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # implement the random forest regressor
    rf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

    # fit the model
    rf.fit(X_train, y_train)

    # fit the model
    classifier = rf.fit(X_train, y_train)

    return classifier 


def predict_forest(text, queried):
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

    # somehow get the queried country. Idk grab it from the front end jazz
    # country = HERE

    # the initial array for the classifier
    initial_array = [sentiment, words, 0, 0, 0]

    # making sure everything is good with the one hot encoding stuff, don't worry 
    def country_to_array(country):
        array = initial_array  
        if country == 'China':
            array[2] = 1
        elif country == 'Russia':
            array[3] = 1
        elif country == 'United States':
            array[4] = 1
        return array

    # calling the function for the one hot encoding
    country_to_array(country)

    # full array
    X = np.array([initial_array])


    # calling the predictor
    prediction = classifier.predict(X)

    return prediction