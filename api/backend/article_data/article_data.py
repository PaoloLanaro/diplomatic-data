from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

article_data = Blueprint('article_data', __name__)

@article_data.route('/article_data', methods=['POST'])
def update_articles():
    current_app.logger.info('PUT /article_data route')
    article_info = request.json
    
    cursor = db.get_db().cursor()
    
    article_id = article_info['id']
    date = article_info['date']
    sent_score = article_info['sent_score']
    text = article_info['text']
    article_country = article_info['article_country']
    query_country = article_info['query_country']
    url = article_info['url']
    safety_index = article_info['safety_index']

    country_code = '''
    SELECT country_id FROM country WHERE UPPER(country_name) = UPPER(article_country)  
    '''

    cursor.execute(country_code)

    article_country_ID = cursor.fetchall()


    query = '''
    UPDATE article SET  article_id = %s, content = %s, country_id = %s, publication_date = %s, article_link = %s
    '''

    data = (article_id, text, article_country_ID, date, url)
    cursor.execute(query, data)
    db.get_db().commit()
    return 'article updated'




