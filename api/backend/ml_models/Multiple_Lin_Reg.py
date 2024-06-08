import pandas as pd
import numpy as np
from backend.db_connection import db
from textblob import TextBlob

df = pd.read_csv('/apicode/backend/assets/Data News Sources.csv')

def clean(news_data):
    """cleans the data and extracts the X and y values that will be used for the model
    
    Args:
        news_data (df): can be either 1-d or 2-d array containing information regarding the training X values
        
    
    Returns:
        X (array): can be either 1-d or 2-d array containing information regarding the training X values
        y (array): a 1-d array whcich includes all corresponding response values to X
    """

    # dropping unnseccassary columns
    news_data = news_data.drop(columns=['Unnamed: 0', 'date', 'url'])

    # adding word count
    news_data['word_count'] = news_data['text'].apply(lambda x: len(x.split()))

    # standardizing values
    not_list = ['text', 'source_country', 'queried_country']
    col_num_list = [col for col in news_data.columns if col not in not_list]

    for feat in col_num_list:
        news_data[feat] = ((news_data[feat] - news_data[feat].mean()) / news_data[feat].std()).round(3)

    # one hot encoding source_country
    news_data = pd.get_dummies(news_data, columns=['source_country'], drop_first=True)

    # isolating X and y values
    X = (news_data.drop(columns=['sentiment', 'text', 'queried_country'])).values 
    y = (news_data['sentiment']).values


    return X, y

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

    # # grabbing the y values and X values
    # cursor = db.get_db().cursor()
    # X_query = 'SELECT x_vals FROM #whichever database the X values are in#' # TODO this sql query
    # cursor.execute(X_query)
    # X_return = cursor.fetchone() # could very well be wrong, just copying other stuff
    # # where we parse all of the strings from the database

    # X_pre_parse = X_return['x_vals'] 

    # X_train = np.array(list(map(float, X_raw[1:, -1].split(','))))
    # y_train = np.array(list(map(float, y_raw[1:, -1].split(','))))


    X = add_bias_column(X_train)
    XtXinv = np.linalg.inv(np.matmul(X.T, X))
    m = np.matmul(XtXinv, np.matmul(X.T, y_train))
    
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