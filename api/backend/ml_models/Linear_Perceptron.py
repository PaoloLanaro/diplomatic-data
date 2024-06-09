import numpy as np
import pandas as pd
from datetime import datetime
from pandas import Timestamp
from collections import Counter
from backend.db_connection import db
import logging
logger = logging.getLogger()
import os

logger.info(f'cwd = {os.getcwd()}') # grabs current working directory

df = pd.read_csv('/apicode/backend/assets/Data News Sources.csv')
df_ss = pd.read_csv('/apicode/backend/assets/safetycodes.csv')

def train():
    """
    Description: Allows linear perceptron model to be trained from scratch 
    in an 'admin' role.

    Args: n/a

    Returns:
        msg (str): 'Training the model'
    """

    return 1.235

def predict(country):
    """
    Description: Using the provided country, predict the sentiment score via various news sources.

    Args: 
        country (str): user's intended country of interest

    Returns:
        sentiment (float): value of +/- 1 that allows for the user to understand general sentiment of their country
    """
    safety_score = df_ss.loc[df_ss['Country'] == country]['Safety Index']
    logger.info(f'safety_score = {safety_score}') # records and stores the current country
    X = np.concatenate((1, safety_score), axis=None) # [1 safety_score]
    
    logger.info(f'current X= {X}')

    # get a database cursor 
    cursor = db.get_db().cursor()
    
    logger.info('reached post cursor connection')

    # get the model params from the database #### TODO LOOK AT THIS SHIT THIS IS IMPORTANT
    query = 'SELECT beta_vals FROM weight_vector ORDER BY sequence_number DESC LIMIT 1'
    cursor.execute(query) 
    return_val = cursor.fetchone() # gets one value
    
    logger.info(f'beta vals: {return_val}')

    w = return_val['beta_vals'] # params = dict
    logging.info(f'params = {w}') # gets beta vals

    # turn the values from the database into a numpy array
    # expect to do some string parsing, typically what we're going to be getting back
    params_array = np.array(list(map(float, w[1:-1].split(',')))) # turns string vars to float
    logging.info(f'params array = {params_array}') # 
   
    logging.info('')
    logging.info(f'X val: {X}')
    logging.info(f'w val: {params_array}')
    logging.info(f'X datatype: {type(X)}')
    logging.info(f'w datatype: {type(params_array)}')
    logging.info('')
    
    prediction = np.dot(X, params_array)

    # less then -1.3 is good, greater is bad (this is so funny)

    analysis = -1 if prediction >= -.13 else 1
    
    return analysis

def linear_perceptron(X, y, w, alpha = 1, max_iter = None):
    """
    Description:
        Determines the vector weight of a linear perceptron that classifies entities into two predetermined classes.
    
    Args:
        X(2D array): bias column of 1s, columns are x features
        y(1D array): lables each X as -1 or 1
        w(array): initial x vector w/ dim = cols of X
        alpha(float): learning rate, default = 1
        max_iter(int): max num of iterations for algorithm to run, default = None
    
    Returns:
        w(1D array): final weight vector, calculated by -(w[0]/w[2]).round(2)} + {-(w[1]/w[2]).round(2)}
    """

    # I will set up the key parameters of the function and then the while loop
    # you are responsible for the rest
    runalg = True
    i = 0
    iter = 0

    while runalg:
                
        # for the current i, make the prediction
        y_hat = np.dot(X[i, :], w)
                    
        # if not correct, update w
        if (y_hat < 0) & (y[i] > 0):
            w = w + alpha * X[i, :]
                
        if (y_hat >= 0) & (y[i] < 0):
            w = w - alpha * X[i, :]

        i += 1 
                
        # if you've just updated the last i (the last observation in the data), add one to iter
        if (i == X.shape[0]):
            i = 0
            iter += 1
                        
        # if you've set a max_iter, and if you've REACHED the max_iter, set runalg = False, print w and iter, and break
        if (iter == max_iter):
            runalg = False
            print(w)
            print(iter)
            break
    
    return w

def label_y_values(y_raw):
    """
    Description: Labels the provided Y values with either -1 or 1 as being correct or incorrect.
    
    Args:
        y_raw (1D array): raw y values straight from the dataframe
        
    Returns:
        y_new(1D array): array of -1s and 1s that represent the "correct" representation of a y value
    """
    y_new = np.empty(len(y_raw))
    
    for y in range(len(y_raw)):
        if y_raw[y] >= 0:
            y_new[y] = 1
        else:
            y_new[y] = -1
    
    return y_new

df['sentiment'] = (df['sentiment'] - df['sentiment'].mean()) / df['sentiment'].mean()
df['Safety Index'] = (df['Safety Index'] - df['Safety Index'].mean()) / df['Safety Index'].mean()

# adding a bias column
Xp = np.column_stack([np.ones(np.array(df['Safety Index']).shape[0]), np.array(df['Safety Index'])])

# labeling the ys
yp = label_y_values(df['sentiment'].to_numpy())

w_test = np.array([0, 1])

w = linear_perceptron(Xp, yp, w_test, alpha=1, max_iter=1000)