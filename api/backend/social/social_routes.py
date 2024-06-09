from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

social = Blueprint('social', __name__)

# to retrieve from the recently viewed tables
@social.route("/recently_viewed", methods=["GET"])
def get_trending():
    current_app.logger.info('GET /recently_viewed route')
    cursor = db.get_db().cursor()

    query = '''
        SELECT a.article_link FROM article a JOIN
        views v ON (a.article_id = v.article_id)
        WHERE v.user_id = anton_id
        ORDER BY v.view_date
        LIMIT 3;
    '''




# to retrieve from the likes tables
# @trending.route('/trending_data', methods=['GET'])
# def find_most_trendy():
#     current_app.logger.info('GET /trending_data route')
#     cursor = db.get_db().cursor()

#     query = '''
#         SELECT *
#         FROM article a 
#         JOIN trending_articles t ON a.article_id = t.article_id 
#         ORDER BY t.views_last_24_hours DESC
#         LIMIT 1;
#     '''
    
#     # object we are using to communicate with the database -> temporary connection to db 
#     cursor.execute(query) 

#     # get the result from the cursor executed query
#     result = cursor.fetchone()

#     # get the text from the article
#     text = result['content']
#     sentiment = result['sentiment']
#     views_last_24_hours = result['views_last_24_hours']
#     current_app.logger.info(f'text={text}')

#     # to convert the article content to a JSON response and return it to the client
#     return jsonify({'content': text, 'sentiment': sentiment, 'views_last_24_hours': views_last_24_hours})


# to retireve fromm the shares tables

# likes routes
@social.route("/likes", methods=["POST"])
def add_likes():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_liked"]

    # Constructing the query
    query = 'INSERT INTO likes (article_id, user_id, like_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    data = (article_id, user_id, date)
    cursor.execute(query, data)
    db.get_db().commit()
    current_app.logger.info(query)

    return "added new likes entry"


@social.route("/likes/<likeID>", methods=["DELETE"])
def remove_likes(likeID):
    current_app.logger.info("DELETE /likes/<likeID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM likes WHERE likes.likes_id = %s"
    cursor.execute(query, (likeID,))
    db.get_db().commit()
    current_app.logger.info(query)

    return "removed likes entry"

# shares routes
@social.route("/shares", methods=["POST"])
def add_shares():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_shared"]

    # Constructing the query 
    query = 'INSERT INTO shares (article_id, user_id, share_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    data = (article_id, user_id, date)
    cursor.execute(query, data)
    db.get_db().commit()
    current_app.logger.info(query)

    return "added new shares entry"


@social.route("/shares/<sharesID>", methods=["DELETE"])
def remove_shares(sharesID):
    current_app.logger.info("DELETE /shares/<sharesID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM shares WHERE shares.shares_id = %s"
    cursor.execute(query, (sharesID,))
    db.get_db().commit()
    current_app.logger.info(query)

    return "removed shares entry"

# saves routes
@social.route("/saves", methods=["POST"])
def add_saves():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_saved"]

    # Constructing the query 
    query = 'INSERT INTO saves (article_id, user_id, save_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    data = (article_id, user_id, date)
    cursor.execute(query, data)
    db.get_db().commit()
    current_app.logger.info(query)

    return "added new saves entry"


@social.route("/saves/<savesID>", methods=["DELETE"])
def remove_saves(savesID):
    current_app.logger.info("DELETE /saves/<savesID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM saves WHERE saves.saves_id= %s"
    cursor.execute(query, (savesID,))
    db.get_db().commit()
    current_app.logger.info(query)

    return "removed saves entry"

@social.route("/user_likes", methods=["POST"])
def add_user_likes():
    current_app.logger.info("POST /user_likes")
    response = request.json
    current_app.logger.info(f'response: {response}')
    user_id = response['user_id']
    article_id = response['article_id']
    like_date = response['like_date']

    add_likes_query = 'INSERT INTO likes (user_id, article_id, like_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(add_likes_query, (user_id, article_id, like_date))
    db.get_db().commit()

    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@social.route("/user_saves", methods=["POST"])
def add_user_saves():
    current_app.logger.info("POST /user_saves")
    response = request.json
    current_app.logger.info(f'response: {response}')
    user_id = response['user_id']
    article_id = response['article_id']
    save_date = response['save_date']

    add_likes_query = 'INSERT INTO saves (user_id, article_id, save_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(add_likes_query, (user_id, article_id, save_date))
    db.get_db().commit()

    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
