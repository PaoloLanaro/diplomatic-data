from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Multiple_Lin_Reg import predict, train
from backend.db_connection import db

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country_origin>/<country_query>', methods=['GET'])
def test_model_one(text, country_origin, country_query):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country_origin>/<country_query>')
    current_app.logger.info(f'text: {text} \ncountry_origin: {country_origin} \country_query: {country_query}')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vector table
    m_query = 'SELECT * FROM beta_vals;'
    cursor.execute(m_query)
    m = [x[0] for x in cursor.description]

    sentiment_guess, sentiment_actual = predict(text, country_origin, country_query, m)

    row_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response # TODO need to actually call the predict function

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

@models.route('/train_prediction1', methods=['GET']) # trains lin reg
def train_prediction1():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    returnVal = train();
    current_app.logger.info(f'called train function from backend, response {returnVal}')
    current_app.logger.info(f'data type of returnVal is {type(returnVal)}')

    # query = 'INSERT INTO weight_vector (beta_vals) VALUES %s'
    # cursor = db.get_db().cursor()
    # cursor.execute(query, (returnVal))

    response = make_response(jsonify(returnVal))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@models.route('/train_prediction2', methods=['GET']) # trains random forest
def train_prediction2():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    returnVal = train();
    current_app.logger.info(f'called train function from backend, response {returnVal}')
    current_app.logger.info(f'data type of returnVal is {type(returnVal)}')

    # query = 'INSERT INTO weight_vector (beta_vals) VALUES %s'
    # cursor = db.get_db().cursor()
    # cursor.execute(query, (returnVal))

    response = make_response(jsonify(returnVal))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
