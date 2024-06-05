from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

social = Blueprint("social", __name__)

# likes routes
@social.route("/likes", method=["POST"])
def add_likes():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_liked"]

    # Constructing the query
    query = 'INSERT INTO likes (article_id, user_id, date_liked) VALUES ("'
    query += article_id + '", "'
    query += user_id + '", "'
    query += date + '", '
    current_app.logger.info(query)
    return "added new likes entry"


@social.route("/likes/<likeID>", method=["DELETE"])
def remove_likes(likeID):
    current_app.logger.info("DELETE /likes/<likeID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM likes WHERE likes.likes_id = likeID"
    cursor.execute(query)
    current_app.logger.info(query)
    return "removed likes entry"

# shares routes
@social.route("/shares", method=["POST"])
def add_shares():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_shared"]

    # Constructing the query
    query = 'INSERT INTO shares (article_id, user_id, date_shared) VALUES ("'
    query += article_id + '", "'
    query += user_id + '", "'
    query += date + '", '
    current_app.logger.info(query)
    return "added new shares entry"


@social.route("/shares/<sharesID>", method=["DELETE"])
def remove_shares(sharesID):
    current_app.logger.info("DELETE /shares/<sharesID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM shares WHERE shares.shares_id = likeID"
    cursor.execute(query)
    current_app.logger.info(query)
    return "removed shares entry"

# saves routes
@social.route("/saves", method=["POST"])
def add_saves():
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable
    article_id = the_data["article_id"]
    user_id = the_data["user_id"]
    date = the_data["date_saved"]

    # Constructing the query
    query = 'INSERT INTO saves (article_id, user_id, date_saved) VALUES ("'
    query += article_id + '", "'
    query += user_id + '", "'
    query += date + '", '
    current_app.logger.info(query)
    return "added new saves entry"


@social.route("/saves/<savesID>", method=["DELETE"])
def remove_saves(savesID):
    current_app.logger.info("DELETE /saves/<savesID>")
    cursor = db.get_db().cursor()
    query = "DELETE FROM saves WHERE saves.saves_id= likeID"
    cursor.execute(query)
    current_app.logger.info(query)
    return "removed saves entry"
