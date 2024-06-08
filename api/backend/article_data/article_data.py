from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

article = Blueprint('article', __name__)

@article.route('/random_article', methods=['GET'])
def get_random_article():
    current_app.logger.info('POST /random_article route')
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
    country_code = str(random_article['source_country']).upper()
    country_name_query = 'SELECT country_name FROM country WHERE UPPER(country_code) = %s'
    cursor.execute(country_name_query, country_code)
    cursor_country_name = cursor.fetchone()
    current_app.logger.info(f'cursor_country_name: {cursor_country_name}')
    if cursor_country_name is None:
        country_name = 'error'
    else:
        country_name = cursor_country_name['country_name']

    data = {
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
    
    calendar_date = article_info['YYYY-MM-DD']
    day_time = article_info['HH:MM:SS']
    date = calendar_date + ' ' + day_time
    text = article_info['text']
    article_country = article_info['article_country']
    queried_country = article_info['query_country']
    url = article_info['url']

    country_code = 'INSERT'

    cursor.execute(country_code)
    article_country_ID = cursor.fetchone()
    cursor.clear_attributes()

    query = 'INSERT INTO article (content, publication_date, article_link, article_country, queried_country) VALUES (%s, %s, %s, %s, %s)'
    data = (text, article_country_ID, date, url)
    current_app.logger.info((query, data))

#   content MEDIUMTEXT,
#   publication_date DATETIME,
#   article_link VARCHAR(200),
#   saftey_index FLOAT, -- make this the forigen key 
#   source_country VARCHAR(100),
#   sentiment FLOAT,
#   queried_country VARCHAR(100)

    cursor.execute(query, data)
    db.get_db().commit()
    return 'article added'




