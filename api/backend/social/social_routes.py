from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

social = Blueprint('social', __name__)

# to retrieve from the recently viewed tables
@social.route("/recently_viewed/<user_id>", methods=["GET"])
def get_recently_viewed(user_id):
    current_app.logger.info('GET /recently_viewed route')
    cursor = db.get_db().cursor()
    
    query = '''
        SELECT * FROM article a JOIN
        views v ON (a.article_id = v.article_id)
        WHERE v.user_id = %s
        ORDER BY v.view_date DESC
        LIMIT 5;
    '''

    # current_app.logger.info()
    cursor.execute(query, user_id)
    result = cursor.fetchall()
    # current_app.logger.info(f'recently viewed result[0] = {result[0]}')

    urls = []
    for row in result:
        d = {'url': row['article_link']}
        urls.append(d)
    current_app.logger.info(f'like urls = {urls}')

    return jsonify(urls)

# to retrieve from the likes table
@social.route("/likes/<user_id>", methods=["GET"])
def get_liked_articles(user_id):
    current_app.logger.info("GET /likes route")
    cursor = db.get_db().cursor()

    query = '''
        SELECT * FROM article a JOIN
        likes l ON (a.article_id = l.article_id)
        WHERE l.user_id = %s
        ORDER BY l.like_date DESC;
    '''

    cursor.execute(query, user_id)
    result = cursor.fetchall()
    # current_app.logger.info(f'likes result[0] = {result[0]}')
    urls = []
    for row in result:
        d = {'url': row['article_link']}
        urls.append(d)
    current_app.logger.info(f'like urls = {urls}')

    return jsonify(urls)

# to retrieve from the saves table
@social.route("/saves/<user_id>", methods=["GET"])
def get_saved_articles(user_id):
    current_app.logger.info("GET /saves route")
    cursor = db.get_db().cursor()

    query = '''
        SELECT * FROM article a JOIN
        saves s ON (a.article_id = s.article_id)
        WHERE s.user_id = %s
        ORDER BY s.save_date DESC;
    '''
    current_app.logger.info(f'type: {type(user_id)}')

    cursor.execute(query, user_id)
    result = cursor.fetchall()
    # current_app.logger.info(f"saves result={type(result[0])}")
    urls = []
    for row in result:
        d = {'url': row['article_link']}
        urls.append(d)
    current_app.logger.info(f'saves urls = {urls}')

    if len(urls) == 0:
        urls.append("You haven't saved any articles yet")

    return jsonify(urls)

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
    like_date = response['date_liked']
    like_date = like_date[0] + ' ' + like_date[1]

    add_likes_query = 'INSERT INTO likes (user_id, article_id, like_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(add_likes_query, (user_id, article_id, like_date))
    db.get_db().commit()

    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@social.route("/user_views", methods=["POST"])
def add_user_views():
    current_app.logger.info('+------------------+')
    current_app.logger.info("POST /user_views")
    response = request.json
    current_app.logger.info(f'response: {response}')
    user_id = response['user_id']
    article_id = response['article_id']
    view_date = response['viewed_at']

    add_dates_query = 'INSERT INTO views (user_id, article_id, view_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(add_dates_query, (user_id, article_id, view_date))
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
    save_date = response['date_saved']
    save_date = save_date[0] + ' ' + save_date[1]

    current_app.logger.info(f'save_date: {save_date}')

    add_likes_query = 'INSERT INTO saves (user_id, article_id, save_date) VALUES (%s, %s, %s)'
    cursor = db.get_db().cursor()
    cursor.execute(add_likes_query, (user_id, article_id, save_date))
    db.get_db().commit()

    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
