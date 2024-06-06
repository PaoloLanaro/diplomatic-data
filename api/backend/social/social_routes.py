from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

social = Blueprint('social', __name__)

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


