from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Multiple_Lin_Reg import predict, train
from backend.db_connection import db
import pandas as pd

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country_origin>', methods=['GET'])
def test_model_one(text, country_origin):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country_origin>/')
    current_app.logger.info(f'text: {text} \ncountry_origin: {country_origin}')

    beta_cursor = db.get_db().cursor()
    # beta_val_query = 'SELECT beta_vals FROM weight_vector ORDER BY sequence_number DESC LIMIT 1'
    beta_val_query = 'SELECT beta_vals FROM weight_vector'
    beta_cursor.execute(beta_val_query)
    beta_val = beta_cursor.fetchall()

    current_app.logger.info(f"ss_query returns: {beta_val}")

    # grabbing the ss values
    ss_cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vector table
    ss_query = 'SELECT * FROM country;'
    ss_cursor.execute(ss_query)
    ss_result = ss_cursor.fetchall()

    sentiment = predict(text, country_origin, ss_result, beta_val)
    current_app.logger.info(f'printing out type {type(sentiment)}')

    the_response = make_response(jsonify({'sentiment_guess': sentiment[0], 'sentiment_actual': sentiment[1]}))
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

    # grabbing all x values
    X_cursor = db.get_db().cursor()
    X_query = 'SELECT content, country_written_from, sentiment, country_written_about, safety_index FROM article JOIN country ON country.country_name = article.country_written_about;'
    X_cursor.execute(X_query)
    current_app.logger.info(f'executed query {X_query} succsefully')
    X_query_return = X_cursor.fetchall()
    train_response = train(X_query_return)
    
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

@models.route('/weight_vector', methods=['POST'])
def add_beta_vals():
    current_app.logger.info('model_routes.py: POST weight_vector') 
    current_app.logger.info(f'request type: {type(request)}')

    beta_vals_list = request.json
    current_app.logger.info(f'response: {beta_vals_list}\ntype(response): {type(beta_vals_list)}')
    beta_vals_string = str(beta_vals_list)

    query = 'INSERT INTO weight_vector (beta_vals) VALUES (%s)'
    cursor = db.get_db().cursor()
    cursor.execute(query, (beta_vals_string))
    current_app.logger.info(f'query: {query}')
    db.get_db().commit()
    
    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

