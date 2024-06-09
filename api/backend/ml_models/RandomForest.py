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
    """
    Cleans up the incoming news data that represents each article.

    Args: 
        news_data(list): list of json such that each item represents an article

    Returns:
        df(pd.DataFrame): containing the above info in readily accessible format
    """

    data = {
        'content': [], 
        'country_written_from': [], 
        'sentiment': [],
        'country_written_about': []
    }

    for item in range(len(news_data) - 1):
        data['content'].append(news_data[item]['content'])
        data['country_written_from'].append(news_data[item]['country_written_from'])
        data['sentiment'].append(news_data[item]['sentiment'])
        data['country_written_about'].append(news_data[item]['country_written_about'])

    df = pd.DataFrame().from_dict(data)

    df['word_count'] = df['content'].apply(lambda x: len(x.split())) # adding word count

    # drop the columns im not using
    df.drop(['content'], axis=1, inplace=True)
    df.dropna(axis=0, inplace=True)

    return df


    # # drop the columns im not using
    # df.drop(['Unnamed: 0', 'date', 'url', 'Safety Index'], axis=1, inplace=True)
    # df.dropna(axis=0, inplace=True)


    # # drop the columns im not using
    # df.drop(['content'], axis=1, inplace=True)
    # df.dropna(axis=0, inplace=True)

    # # one hot encoding
    # df = pd.get_dummies(news_data, columns=['country_written_about'], drop_first=True)

    # # X and y
    # X = news_data.drop(columns=['source_country']) 
    # y = news_data['source_country']

    # return X, y

def extract_x_y(df):
    """cleans the data and extracts the X and y values that will be used for the model
    
    Args:
        news_data (df): can be either 1-d or 2-d array containing information regarding the training X values
        
    
    Returns:
        X (array): can be either 1-d or 2-d array containing information regarding the training X values
        y (array): a 1-d array whcich includes all corresponding response values to X
    """


    # one hot encoding
    df = pd.get_dummies(df, columns=['country_written_about'], drop_first=True)

    # X and y
    X = df.drop(columns=['source_country']) 
    y = df['source_country']


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


def predict_rf(text, classifier):
    """
    Description: Using the sentiment score, word count, and queried country, predicting the source country 

    Args: 
        text(string): text used to find the sentiment score and word count
        classifier(idk): the rf classifier that was made in the training function

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

    # somehow get the queried country. Idk 
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