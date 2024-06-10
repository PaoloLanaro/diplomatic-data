from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

preference = Blueprint('preference', __name__)

@preference.route('/preference_routes', methods=['POST'])
def add_user_preferences():
    current_app.logger.info('preference_routes.py: POST preferences') 
    current_app.logger.info(f'request type: {type(request)}')

    preferences = request.json
    current_app.logger.info(f'response: {preferences}\ntype(response): {type(preferences)}')
    user_id = preferences['user_id']
    start_date = preferences['start_date']
    end_date = preferences['end_date']
    country_traveling_to = preferences['country_traveling_to']
    country_traveling_from = preferences['country_traveling_from']

    query = 'INSERT INTO filter (user_id, start_date, end_date, country_traveling_to, country_traveling_from) VALUES (%s, %s, %s, %s, %s)'
    cursor = db.get_db().cursor()
    data = (user_id, start_date, end_date, country_traveling_to, country_traveling_from)
    cursor.execute(query, data)
    current_app.logger.info(f'query: {query}')
    db.get_db().commit()
    current_app.logger.info(query)

    return "added user preferences"





