import pandas as pd
import numpy as np
from backend.db_connection import db
from textblob import TextBlob
from flask import current_app

def clean(news_data):
    """
    Cleans up the incoming news data that represents each article.

    Args: 
        news_data(list): list of json such that each item represents an article

    Returns:
        dataframe(pd.DataFrame): containing the above info in readily accessible format
    """

    # content, country_written_from, sentiment, country_written_about, safety_index
    data = {
        'content': [], 
        'country_written_from': [], 
        'sentiment': [],
        'country_written_about': [], 
        'safety_index': []
    }

    for item in range(len(news_data) - 1):
        data['content'].append(news_data[item]['content'])
        data['country_written_from'].append(news_data[item]['country_written_from'])
        data['sentiment'].append(news_data[item]['sentiment'])
        data['country_written_about'].append(news_data[item]['country_written_about'])
        data['safety_index'].append(news_data[item]['safety_index'])

    df = pd.DataFrame().from_dict(data)

    df['word_count'] = df['content'].apply(lambda x: len(x.split())) # adding word count

    return df

def clean_ss(country, ss_data):
    """
    With the provided country, return the safety score.

    Args:
        country (str): country of origin of user's input
        ss_data (list): list of json of country's input

    Return:
        safety_score (float): safety score of user's indicated country
    """

    data = {
        'country_name': [], 
        'safety_index': []
    }

    for item in range(len(ss_data) - 1):
        data['country_name'].append(ss_data[item]['country_name'])
        data['safety_index'].append(ss_data[item]['safety_index'])

    df = pd.DataFrame().from_dict(data)

    country_row = df[df['country_name'] == country]

    return country_row['safety_index'].values[0]

def train(data):
    """takes in 2 raw training arrays and gives the vector containing the coefficients for the line of best fit
    
    Args:
        data (json): return of the api request
        ss_data(json): return of the ss request
    
    Returns:
        m (array): coefficents for the line of best fit
    """

    df = clean(data)

    current_app.logger.info(f"checking df cols: {df.columns}")

    not_list = ['content', 'country_written_from', 'country_written_about']
    col_num_list = [col for col in df.columns if col not in not_list]

    for feat in col_num_list:
        df[feat] = ((df[feat] - df[feat].mean()) / df[feat].std()).round(3)
    
    df = pd.get_dummies(df, columns=['country_written_from'], drop_first=True)

    for col in df.select_dtypes(include='bool').columns:
        df[col] = df[col].astype(float)

    y = df['sentiment'].values

    df = df.drop(columns=['content', 'sentiment', 'country_written_about'])

    current_app.logger.info(f"checking df cols: {df.columns}")

    X_prep = (df).values

    X = add_bias_column(X_prep)

    XtXinv = np.linalg.inv(np.matmul(X.T, X))
    m = np.matmul(XtXinv, np.matmul(X.T, y))

    return m # needs to be stored and then queried from the function below

# predict
def predict(text, country, country_about, ss_raw, m_raw):
    """
    Description:
        With the user specified values, we predict the sentiment of an article.

    Args:
        text(str): corpus for analysis of both library version of sentiment and for finding the word count as feature of model
        country (str): intended country of safety score for use in sentiment prediction, to be parsed for a value
        m_pre_parse (str): weight vectors of the linear regression

    Returns:
        dot prod (float): calculation of the provided x values with the m values
        sentiment(float): of a hypothetical article using textblob library
    """

    # actual sentiment
    sentiment = TextBlob(text).sentiment.polarity

    m_raw_array = m_raw[0]['beta_vals']

    m = np.array(list(map(float, m_raw_array[1:-1].split(',')))) 

    X = update_country_value(country, text, clean_ss(country_about, ss_raw))

    return np.dot(X, m), sentiment

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

# getting a proper X array to multiply by
def update_country_value(country, text, safety_score):
    """
    Determines the X values that need to be inside multiplies. 
    """
    sc_col = ['safety_score', 'word_count','source_country_GB', 'source_country_au', 'source_country_be',
       'source_country_bh', 'source_country_bm', 'source_country_ca',
       'source_country_cn', 'source_country_de', 'source_country_eg',
       'source_country_es', 'source_country_et', 'source_country_eu',
       'source_country_fm', 'source_country_fr', 'source_country_gb',
       'source_country_gy', 'source_country_hk', 'source_country_ie',
       'source_country_in', 'source_country_ir', 'source_country_it',
       'source_country_jp', 'source_country_ke', 'source_country_kz',
       'source_country_lb', 'source_country_lk', 'source_country_mv',
       'source_country_mx', 'source_country_my', 'source_country_ng',
       'source_country_pk', 'source_country_qa', 'source_country_ru',
       'source_country_se', 'source_country_sg', 'source_country_so',
       'source_country_tv', 'source_country_us', 'source_country_uy',
       'source_country_uz']
    
    array = np.zeros(41) # will always be of len 43 because the 'm' array is always 43 features
    array = np.insert(array, 0, safety_score) # NEED SAFETY SCORE FROM WHEREVER
    array = np.insert(array, 1, len(text.split())) 

    # Create the full column name for the country
    country_column = f'source_country_{country}'
    # Check if the column exists in sc_col
    if country_column in sc_col:
        # Get the index of the country column
        index = sc_col.index(country_column)
        # Update the corresponding value in the array from 0 to 1
        array[index] = 1
    else:
        print(f"Country column '{country_column}' does not exist in the columns list.")
    return array