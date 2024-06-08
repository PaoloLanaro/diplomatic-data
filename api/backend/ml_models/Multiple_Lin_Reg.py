import pandas as pd
import numpy as np
from backend.db_connection import db
import logging
import os
from sklearn.model_selection import train_test_split

logger = logging.getLogger()


df = pd.read_csv('/apicode/backend/assets/Data News Sources.csv')

# train 
def train():
    """takes in 2 arrays and gives the vector containing the coefficients for the line of best fit
    
    Args:
        X (array): can be either 1-d or 2-d
        y (array): a 1-d array whcich includes all corresponding response values to X
    
    Returns:
        m (array): coefficents for the line of best fit
    """
    # grabbing the y values and X values
    cursor = db.get_db().cursor()
    X_query = 'SELECT x_vals FROM #whichever database the X values are in#'
    cursor.execute(X_query)
    X_return = cursor.fetchone() # could very well be wrong, just copying other stuff
    # where we parse all of the strings from the database

    X = add_bias_column(X_train)
    XtXinv = np.linalg.inv(np.matmul(X.T, X))
    m = np.matmul(XtXinv, np.matmul(X.T, y))
    
    return m # needs to be stored and then queried from the function below

# predict
def predict(text, country, hour, month):
    """
    Description:
        With the user specified values, we predict the sentiment of an article.

    Args:
        text(str): corpus for analysis of both library version of sentiment and for finding the word count as feature of model
        country(str): intended country of safety score for use in sentiment prediction
        hour(int): hour of publication, [0, 23]
        month(int): month of publication, [1, 12]

    Returns:
        sentiment(float): of a hypothetical article
    """

    # grab database curson
    cursor = db.get_db().cursor()

    m = [] # the sequal qeury of the bias vector

    safety_score = 0 # also the sequal query to the country codes thing!!!!

    X = np.array([1, len(text.split()), safety_score, hour, month])

    return np.dot(add_bias_column(X), m)

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