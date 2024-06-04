from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

article_data = Blueprint('article_data', __name__)

@article_data.route('/article_data', methods=['POST'])
def update_articles():
    current_app.logger.info('PUT /article_data route')
    article_info = request.json
    
    article_id = article_info['id']
    date = article_info['date']
    sent_score = article_info['sent_score']
    text = article_info['text']
    article_country = article_info['article_country']
    query_country = article_info['query_country']
    url = article_info['url']
    safety_index = article_info['safety_index']

    query = '''
    UPDATE article SET  article_id = %s, content = %s, country_id = %s, 
    '''
