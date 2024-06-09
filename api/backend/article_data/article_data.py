from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

article = Blueprint('article', __name__)

@article.route('/random_article', methods=['GET'])
def get_random_article():
    current_app.logger.info('GET /random_article route')
    # GET request
    # get random article from database
      # possibly try and get a title and summary

    # get a random article from within the article table
    cursor = db.get_db().cursor()
    query = 'SELECT * FROM article ORDER BY RAND() LIMIT 1'
    cursor.execute(query) 
    random_article = cursor.fetchone()
    current_app.logger.info(f'random_article {random_article}')

    # date time object to YYYY-MM-DD
    date = str(random_article['publication_date']).split(' ')[0]
    
    # close and reset the cursor
    cursor.close()
    cursor = db.get_db().cursor()

    # country code to country name
    country_code = str(random_article['country_written_from']).upper()
    country_name_query = 'SELECT country_name FROM country WHERE UPPER(country_code) = %s'
    cursor.execute(country_name_query, country_code)
    cursor_country_name = cursor.fetchone()
    current_app.logger.info(f'cursor_country_name: {cursor_country_name}')
    if cursor_country_name is None:
        country_name = 'error'
    else:
        country_name = cursor_country_name['country_name']

    data = {
            'article_id': random_article['article_id'],
            'text': random_article['content'],
            'YYYY-MM-DD': date,
            'link': random_article['article_link'],
            'country_written_from': country_name
            }

    response = make_response(jsonify(data))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

# to add the user's article to the article table 
@article.route('/article_data', methods=['POST'])
def add_new_article():
    current_app.logger.info('POST /article_data route')
    article_info = request.json
    current_app.logger.info(article_info)

    cursor = db.get_db().cursor()
    
    # to get the date and time written
    calendar_date = article_info['YYYY-MM-DD']
    day_time = article_info['HH:MM:SS']
    date = calendar_date + ' ' + day_time

    # to get the article text
    text = article_info['text']

    # to get the the country written about/from
    country_written_about = article_info['country_written_about']
    country_written_from = article_info['country_written_from']

    # convert country written about to short form
    country_name_query = 'SELECT country_code FROM country WHERE UPPER(country_name) = %s'
    cursor.execute(country_name_query, country_written_from.upper())
    cursor_country_name = cursor.fetchone()
    current_app.logger.info(f'cursor_country_name: {cursor_country_name}')
    if cursor_country_name is None:
        country_code = 'error'
    else:
        country_code = cursor_country_name['country_code']
 

    # to get the article info 
    url = article_info['url']

    sentiment = TextBlob(text).sentiment.polarity 

    query = 'INSERT INTO article (content, publication_date, article_link, country_written_from, sentiment, country_written_about) VALUES (%s, %s, %s, %s, %s, %s)'
    data = (text, date, url, country_code, sentiment, country_written_about)
    current_app.logger.info((query, data))

    cursor.execute(query, data)
    db.get_db().commit()
    return 'article added'

@article.route('/articles', methods=['POST'])
def get_articles_matching_search():
    current_app.logger.info('POST /article_data route')
    search_words = request.json
    # should return a python list of data
    current_app.logger.info(search_words)
    conditions = " AND ".join([f'content LIKE "% {keyword} %"' for keyword in search_words])

    # Get atricles, publication dates, URLs, and country_names for articles that match all serach terms
    get_articles_query = f'''
    SELECT content, publication_date, article_link AS url, country_name 
    FROM article 
    JOIN country ON UPPER(country.country_code) = UPPER(article.country_written_from) 
    WHERE {conditions} LIMIT 10'''

    current_app.logger.info(f'get_article_query: {get_articles_query}')
    cursor = db.get_db().cursor()
    cursor.execute(get_articles_query)

    searched_articles = cursor.fetchall()

    the_response = make_response(jsonify(searched_articles))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@article.route('/title/<path:url>', methods=['GET'])
def get_articles_title_from_url(url):
    current_app.logger.info('GET /title route')
    try:
        # Send a GET request to the URL
        current_app.logger.info(f'url: {url}')
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title tag
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = None
            response.raise_for_status()
        
        data = {'title': title}
        response = make_response(jsonify(data))
        response.status_code = 200
        response.mimetype = 'application/json'
        return response
    
    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"
        data = {'error': error_message}
        response = make_response(jsonify(data))
        response.status_code = 400
        response.mimetype = 'application/json'
        return response
