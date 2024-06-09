from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Multiple_Lin_Reg import predict, train
from backend.db_connection import db
import pandas as pd

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country_origin>/<country_query>', methods=['GET'])
def test_model_one(text, country_origin, country_query):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country_origin>/<country_query>')
    current_app.logger.info(f'text: {text} \ncountry_origin: {country_origin} \country_query: {country_query}')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vector table
    query = 'SELECT * FROM article;'
    cursor.execute(query)

    sentiment_guess, sentiment_actual = predict(text, country_origin, country_query, query)

    row_headers = [x[0] for x in cursor.description]
    current_app.logger.info(f'row_headers: {row_headers}')
    json_data = []
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
    cursor = db.get_db().cursor()

    query = 'SELECT * FROM article'
    cursor.execute(query)
    current_app.logger.info(f'executed query {query} succsefully')
    
    query_return = cursor.fetchall()
    current_app.logger.info(f'query_return type: {type(query_return)}')
    current_app.logger.info(f'query_return keys: {query_return[1].keys()}')
    current_app.logger.info(f'checking data type: {type(query_return[1]["sentiment"])}')

    ss_query = 'SELECT * FROM country'
    cursor.execute(ss_query)
    ss_return = cursor.fetchall()
    current_app.logger.info(f'grabbed the ss: {ss_return[1].keys()}')

    train_response = train(query_return, ss_return)
    
    response = make_response(jsonify(train_response))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@models.route('/train_prediction2', methods=['GET']) # trains random forest
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
