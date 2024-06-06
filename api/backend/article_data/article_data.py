from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

article = Blueprint('article', __name__)

# to add the user's article to the article table 
<<<<<<< HEAD
@article.route('/article_data', methods=['POST'])
=======
@article_data.route('/article_data', methods=['POST'])
>>>>>>> 6082d2c70efd6268ada209d7203d2988fbff3a29
def add_new_article():
    current_app.logger.info('POST /article_data route')
    article_info = request.json
    current_app.logger.info(article_info)

    cursor = db.get_db().cursor()
    
<<<<<<< HEAD
    calendar_date = article_info['YYYY-MM-DD']
    day_time = article_info['HH:MM:SS']
    date = calendar_date + ' ' + day_time
=======
    date = article_info['date']
>>>>>>> 6082d2c70efd6268ada209d7203d2988fbff3a29
    text = article_info['text']
    article_country = article_info['article_country']
    queried_country = article_info['query_country']
    url = article_info['url']

<<<<<<< HEAD
    country_code = 'INSERT'
=======
    country_code = '''
    INSERT 
    '''
>>>>>>> 6082d2c70efd6268ada209d7203d2988fbff3a29

    cursor.execute(country_code)
    article_country_ID = cursor.fetchone()
    cursor.clear_attributes()

<<<<<<< HEAD
    query = 'INSERT INTO article (content, publication_date, article_link, article_country, queried_country) VALUES (%s, %s, %s, %s, %s)'
=======
    query = '''
    INSERT INTO article (content, publication_date, article_link, article_country, queried_country) VALUES (%s, %s, %s, %s, %s)
    '''
>>>>>>> 6082d2c70efd6268ada209d7203d2988fbff3a29
    data = (text, article_country_ID, date, url)
    current_app.logger.info((query, data))

    cursor.execute(query, data)
    db.get_db().commit()
    return 'article added'




