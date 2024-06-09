from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from textblob import TextBlob

trending = Blueprint('trending', __name__)

# to add the user's article to the article table 
@trending.route('/trending_data', methods=['GET'])
def find_most_trendy():
    current_app.logger.info('GET /trending_data route')
    cursor = db.get_db().cursor()

    query = '''
        SELECT *
        FROM article a 
        JOIN trending_articles t ON a.article_id = t.article_id 
        ORDER BY t.views_last_24_hours DESC
        LIMIT 1;
    '''
    
    # object we are using to communicate with the database -> temporary connection to db 
    cursor.execute(query) 

    # get the result from the cursor executed query
    result = cursor.fetchone()

    # get the text from the article
    text = result['content']
    sentiment = result['sentiment']
    views_last_24_hours = result['views_last_24_hours']
    current_app.logger.info(f'text={text}')

    # to convert the article content to a JSON response and return it to the client
    return jsonify({'content': text, 'sentiment': sentiment, 'views_last_24_hours': views_last_24_hours})




    
