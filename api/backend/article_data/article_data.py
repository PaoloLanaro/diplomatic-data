from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from textblob import TextBlob

article = Blueprint('article', __name__)

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

    # to get the article info 
    url = article_info['url']

    sentiment = TextBlob(text).sentiment.polarity 

    # country_code = 'INSERT'

    # cursor.execute(country_code)
    # article_country_ID = cursor.fetchone()
    # cursor.clear_attributes()

    query = 'INSERT INTO article (content, publication_date, article_link, country_written_from, sentiment, country_written_about) VALUES (%s, %s, %s, %s, %s, %s)'
    data = (text, date, url, country_written_about, sentiment, country_written_from)
    current_app.logger.info((query, data))

    cursor.execute(query, data)
    db.get_db().commit()
    return 'article added'




