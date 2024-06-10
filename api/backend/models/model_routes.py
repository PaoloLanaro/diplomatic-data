from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Multiple_Lin_Reg import predict, train
from backend.ml_models.RandomForest import predict_rf, train_rf
from backend.db_connection import db
import pandas as pd

models = Blueprint('models', __name__)

@models.route('/prediction1/<text>/<country_origin>/<country_about>', methods=['GET'])
def test_model_one(text, country_origin, country_about):
    current_app.logger.info('model_routes.py: GET /prediction1/<text>/<country_origin>/<country_about>')
    current_app.logger.info(f'text: {text} \ncountry_origin: {country_origin} \ncountry_about: {country_about}')

    beta_cursor = db.get_db().cursor()
    beta_val_query = 'SELECT beta_vals FROM weight_vector ORDER BY sequence_number DESC LIMIT 1'
    beta_cursor.execute(beta_val_query)
    beta_val = beta_cursor.fetchall()

    current_app.logger.info(f"beta val returns: {beta_val}")

    # grabbing the ss values
    ss_cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1; -- for beta vals that are gonna be added to a weight_vector table
    ss_query = 'SELECT * FROM country;'
    ss_cursor.execute(ss_query)
    ss_result = ss_cursor.fetchall()

    sentiment = predict(text, country_origin, country_about, ss_result, beta_val)

    current_app.logger.info(f'printing out type {type(sentiment)}')
    current_app.logger.info(f'printing out sentiment {sentiment}')

    the_response = make_response(jsonify({'sentiment_guess': sentiment[0], 'sentiment_actual': sentiment[1]}))
    current_app.logger.info(f'printing out the response in json {the_response}')
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@models.route('/prediction2/<text>/<queried_country>', methods=['GET'])
def test_model_two(text, queried_country):
    current_app.logger.info('model_routes.py: GET /prediction2/<text>/<queried_country>')
    cursor = db.get_db().cursor()
    # ORDER BY sequence_number DESC LIMIT 1;
    query = 'SELECT content, country_written_about, sentiment, country_written_from FROM article;'
    cursor.execute(query)
    x_data = cursor.fetchall()

    train_return = predict_rf(text, queried_country, x_data)
    current_app.logger.info(f'x data {train_return}')

    the_response = make_response(jsonify(list(train_return)))
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

    cursor = db.get_db().cursor()
    query = 'SELECT content, country_written_about, sentiment FROM article;'
    cursor.execute(query)

    query_return = cursor.fetchall()
    current_app.logger.info(f'return from the query {query_return}')

    train_output = train_rf(query_return)
    current_app.logger.info(f'grabbing the return of the trainer {train_output}')
    response = make_response(jsonify(train_output))

    current_app.logger.info(f'responses from the train function: {response}')

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

