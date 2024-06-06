from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

article_data = Blueprint('article_data', __name__)

# to add the user's article to the article table 
@article_data.route('/article_data', methods=['POST'])
def add_new_article():
    current_app.logger.info('POST /article_data route')
    article_info = request.json
    current_app.logger.info(article_info)

    cursor = db.get_db().cursor()
    
    date = article_info['date']
    text = article_info['text']
    article_country = article_info['article_country']
    queried_country = article_info['query_country']
    url = article_info['url']

    country_code = '''
    INSERT 
    '''

    cursor.execute(country_code)
    article_country_ID = cursor.fetchone()
    cursor.clear_attributes()

    query = '''
    INSERT INTO article (content, publication_date, article_link, article_country, queried_country) VALUES (%s, %s, %s, %s, %s)
    '''
    data = (text, article_country_ID, date, url)
    current_app.logger.info((query, data))

    cursor.execute(query, data)
    db.get_db().commit()
    return 'article added'




