from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Multiple_Lin_Reg import predict, train
from backend.db_connection import db
import pandas as pd

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country_origin>', methods=['GET'])
def test_model_one(text, country_origin, country_query):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country_origin>/')
    current_app.logger.info(f'text: {text} \ncountry_origin: {country_origin}')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vector table
    query = 'SELECT * FROM beta_vals;' # TODO check with paolo if this is correct
    cursor.execute(query)

    m_result = cursor.fetchall()

    sentiment_guess, sentiment_actual = predict(text, country_origin, m_result)

    the_response = make_response(jsonify({'sentiment_guess': sentiment_guess, 'sentiment_actual': sentiment_actual}))
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

@models.route('/train_prediction1', methods=['GET']) # trains lin reg
def train_prediction1():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    cursor = db.get_db().cursor()

    query = 'SELECT content, country_written_from, sentiment, country_written_about, safety_index FROM article JOIN country ON country.country_name = article.country_written_about;'
    cursor.execute(query)
    current_app.logger.info(f'executed query {query} succsefully')
    
    query_return = cursor.fetchall()

    train_response = train(query_return)
    
    response = make_response(jsonify(train_response.tolist()))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@models.route('/train_prediction2', methods=['GET']) # trains random forest
def train_prediction2():
    current_app.logger.info('model_routes.py: GET /train_prediction1')
    returnVal = train()
    current_app.logger.info(f'called train function from backend, response {returnVal}')
    current_app.logger.info(f'data type of returnVal is {type(returnVal)}')

    response = make_response(jsonify(returnVal))
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
