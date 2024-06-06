from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

activity = Blueprint('activity', __name__)

# route to put data into filters table
@activity.route('/filters', methods=['PUT'])
def put_filters():
    current_app.logger.info('activity.py: PUT /filters')
    filter_info = request.json
    filter_id = filter_info['filter_id']
    user_id = filter_info['user_id']
    start_date = filter_info['start_date']
    end_date = filter_info['end_date']
    country_about = filter_info['country_about']
    country_from = filter_info['country_from']

    query = 'UPDATE filters SET start_date = %s, end_date = %s, country_about = %s, country_from = %s WHERE user_id = %s'
    data = (start_date, end_date, country_about, country_from, user_id)
    cursor = db.get_db().cursor
    cursor.execute(query, data)
    db.get_db.commit()
    return 'filters_table updated'

# route to get data from recently viewed table
@activity.route('/recently_viewed', methods=['GET'])
def get_recently_viewed():
    current_app.logger.info('activity.py: GET /filters')
    cursor = db.get_db().cursor()
    query = 'SELECT * from recently_viewed'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall() 
    for row in theData:
        json_data.append(dict(zip(row_headers, row))) 
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    return the_response
    

# route to get data from trending_articles table
@activity.route('/trending_articles', methods=['GET'])
def get_trending_articles():
    current_app.logger.info('activity.py: GET /filters')
    cursor = db.get_db().cursor()
    query = 'SELECT * from trending_articles'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
