from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Linear_Perceptron import predict, train
from backend.db_connection import db

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country>/<month>/<hour>', methods=['GET'])
def test_model_one(text, country, month, hour):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country>/<month>/<hour>')
    current_app.logger.info(f'\ntext: {text} \ncountry: {country} \nmonth: {month} \nhour: {hour}')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vecto table
    # query = 'SELECT beta_vals FROM weight_vector ORDER BY sequence_number DESC LIMIT 1'
    query = 'SELECT * from users'
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    current_app.logger.info(f'row_headers: {row_headers}')
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@models.route('/prediction2/<possibleVar>', methods=['GET'])
def test_model_two(possibleVar):
    current_app.logger.info('model_routes.py: GET /prediction2/<possibleVar>')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1;
    query = 'SELECT * from users;'
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

@models.route('/train_prediction1', methods=['GET'])
def train_prediction1():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    returnVal = train()
    current_app.logger.info(f'called train function from backend, response {returnVal}')
    current_app.logger.info(f'data type of returnVal is {type(returnVal)}')

    # query = 'INSERT INTO weight_vector (beta_vals) VALUES %s'
    # cursor = db.get_db().cursor()
    # cursor.execute(query, (returnVal))

    response = make_response(jsonify(returnVal))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@models.route('/train_prediction2', methods=['GET'])
def train_prediction2():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    returnVal = train()
    current_app.logger.info(f'called train function from backend, response {returnVal}')
    current_app.logger.info(f'data type of returnVal is {type(returnVal)}')

    # query = 'INSERT INTO weight_vector (beta_vals) VALUES %s'
    # cursor = db.get_db().cursor()
    # cursor.execute(query, (returnVal))

    response = make_response(jsonify(returnVal))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
