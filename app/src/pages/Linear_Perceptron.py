import numpy as np
import pandas as pd
from datetime import datetime
from pandas import Timestamp
from collections import Counter

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
    no_improvement_count = 0 # chat gpt
    best_loss = float('inf') # chat gpt
    best_w = np.copy(w) # chat gpt

    while runalg:
                
        # for the current i, make the prediction
        y_hat = np.dot(X[i, :], w)
        
        # calculate loss
        loss = max(0, 1 - y[i] * y_hat) # chat gpt
            
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
            
            total_loss = np.sum([max(0, 1 - y[j] * np.dot(X[j, :], w)) for j in range(X.shape[0])]) / X.shape[0]
            
            if total_loss < best_los
            
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

df = pd.read_csv('Data News Sources.csv')

df['sentiment'] = (df['sentiment'] - df['sentiment'].mean()) / df['sentiment'].mean()
df['Safety Index'] = (df['Safety Index'] - df['Safety Index'].mean()) / df['Safety Index'].mean()

# adding a bias column
Xp = np.column_stack([np.ones(np.array(df['Safety Index']).shape[0]), np.array(df['Safety Index'])])

# labeling the ys
yp = label_y_values(df['sentiment'].to_numpy())

w_test = np.array([0, 1])

w =  linear_perceptron(Xp, yp, w_test, alpha=1, max_iter=1000)