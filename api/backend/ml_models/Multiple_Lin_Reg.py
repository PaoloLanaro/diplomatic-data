import pandas as pd
import numpy as np
from backend.db_connection import db
from textblob import TextBlob
import logging
import os
from sklearn.model_selection import train_test_split

logger = logging.getLogger()


df = pd.read_csv('/apicode/backend/assets/Data News Sources.csv')

# train 
def train(df):
    """takes in 2 raw training arrays and gives the vector containing the coefficients for the line of best fit
    
    Args:
        X_raw (string): can be either 1-d or 2-d array containing information regarding the training X values
        y_raw (string): a 1-d array whcich includes all corresponding response values to X
    
    Returns:
        m (array): coefficents for the line of best fit
    """

    # TODO  P AND M GET DATA BASE THINGS




    
    return m # needs to be stored and then queried from the function below

# predict
def predict(text, ss_pre_parse, m_pre_parse):
    """
    Description:
        With the user specified values, we predict the sentiment of an article.

    Args:
        text(str): corpus for analysis of both library version of sentiment and for finding the word count as feature of model
        ss_pre_parse (str): intended country of safety score for use in sentiment prediction, to be parsed for a value
        m_pre_parse (str): weight vectors of the linear regression

    Returns:
        dot prod (float): calculation of the provided x values with the m values
        sentiment(float): of a hypothetical article using textblob library
    """

    # sentiment
    sentiment = TextBlob(text).sentiment.polarity

    # # grabbing the M vector
    # m_query = 'SELECT m_vals FROM weight_vector ' # TODO flesh this out, not finished
    # cursor.execute(m_query)
    # m_return = cursor.fetchone()
    # m_pre_parse = m_return['m_vals']
    m = np.array(list(map(float, m_pre_parse[1:-1].split(','))))

    # # grabbing the safety score
    # ss_query = 'SELECT safety_index FROM country' # TODO flesh this out and pimp out this db
    # cursor.execute(ss_query)
    # ss_return = cursor.fetchone()
    # ss_pre_parse = ss_return['ss'] # also likely wrong
    safety_score = map(float, ss_pre_parse[1:-1].split(',')) # also the sequal query to the country codes thing!!!!

    X = np.array([1, len(text.split()), safety_score])

    return np.dot(add_bias_column(X), m), sentiment

# adding bias column
def add_bias_column(X):
    """
    Description: Adds bias column to X vector to add an intercept to the line.

    Args:
        X (array): can be either 1-d or 2-d
    
    Returns:
        Xnew (array): the same array, but 2-d with a column of 1's in the first spot
    """
    
    # If the array is 1-d
    if len(X.shape) == 1:
        Xnew = np.column_stack([np.ones(X.shape[0]), X])
    
    # If the array is 2-d
    elif len(X.shape) == 2:
        bias_col = np.ones((X.shape[0], 1))
        Xnew = np.hstack([bias_col, X])
        
    else:
        raise ValueError("Input array must be either 1-d or 2-d")

    return Xnew
