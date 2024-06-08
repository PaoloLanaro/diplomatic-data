import pandas as pd
import numpy as np
from backend.db_connection import db
from textblob import TextBlob

df = pd.read_csv('/apicode/backend/assets/Data News Sources.csv')

def clean(news_data):
    """cleans the data and extracts the X and y values that will be used for the model

    Args:
        news_data (list of json): list of json values with each item being its own separate article

    Returns:
        X_raw (string): can be either 1-d or 2-d array containing information regarding the training X values
        y_raw (string): a 1-d array whcich includes all corresponding response values to X
    """
    df = pd.DataFrame()

    data = {
        'article_id': [], 
        'content': [], 
        'publication_date': [], 
        'article_link': [],
        'country_written_from': [], 
        'sentiment': [],
        'country_written_about': []
    }

    for item in news_data:
        data['article_id'].append(news_data[item]['article'])
        data['content'].append(news_data[item]['content'])
        data['publication_date'].append(news_data[item]['publication_date'])
        data['article_link'].append(news_data[item]['article_link'])
        data['country_written_from'].append(news_data[item]['country_written_from'])
        data['sentiment'].append(news_data[item]['sentiment'])
        data['country_written_about'].append(news_data[item]['country_written_about'])

    return pd.DataFrame.from_dict(data)

def clean_safety_score(ss_data):
    """
    Takes in raw json for the safety score json and produces a dataframe of each country with each different associated safety score.

    Args:
        ss_data (json): contains contents of countries database

    Returns:
        df (DataFrame): contains contents of countries database in easy to use dataframe format
    """
    df = pd.DataFrame()

    data = {
        'country_id': [], 
        'country_name': [], 
        'safety_index': [], 
        'country_code': []
    }

    for country in ss_data:
        data['country_id'].append(ss_data[country][''])

    return df

# train 
# def train(data, ss_data):
def train(data):
    """takes in 2 raw training arrays and gives the vector containing the coefficients for the line of best fit
    
    Args:
        data (json): return of the api request
        ss_data(json): return of the ss request
    
    Returns:
        m (array): coefficents for the line of best fit
    """

    df = clean(data)

    X = add_bias_column(np.array([df['content'], ]))

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