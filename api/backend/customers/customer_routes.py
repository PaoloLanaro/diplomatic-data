########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
# from backend.ml_models.Linear_Perceptron import predict
from backend.ml_models.Multiple_Lin_Reg import predict
from backend.db_connection import db
import numpy as np

customers = Blueprint('customers', __name__)

# gets the user's various input values for the multi linear regression --> model
# calls the ml model
@customers.route('/sentiment_prediction/<text>/<country>/<month>/<hour>', methods=['GET'])
def predict_sentiment(text, country, month, hour):
    # logging the user input values
    current_app.logger.info(f'text: {text}')
    current_app.logger.info(f'country: {country}')
    current_app.logger.info(f'month: {month}')
    current_app.logger.info(f'hour: {hour}')
    sentiment = predict(text, country, month, hour)
    response = make_response(jsonify(sentiment))
    response.status_code = 200
    # mimetype: tells user the kind of data being returned, in this case JSON
    response.mimetype = 'application/json' 
    return response

# # to get a country value for the user asking for ML regression data
# # THIS ROUTE CALLS THE ML MODEL 
# @customers.route('/prediction/<country01>', methods=['GET'])
# def predict_country_sentiment(country01):
#     current_app.logger.info(f'country01 = {country01}')
#     CountryVal = predict(country01)
#     countryVal_response = make_response(jsonify(CountryVal))
#     countryVal_response.status_code = 200
#     countryVal_response.mimetype = 'application/json'
#     return countryVal_response

# Get all customers from the DB
@customers.route('/users', methods=['GET'])
def get_customers():
    current_app.logger.info('customer_routes.py: GET /customers')
    cursor = db.get_db().cursor()
    cursor.execute('select id, company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customers.route('/users', methods=['PUT'])
def update_customer():
    current_app.logger.info('PUT /customers route')
    cust_info = request.json
    # current_app.logger.info(cust_info)
    cust_id = cust_info['id']
    first = cust_info['first_name']
    last = cust_info['last_name']
    company = cust_info['company']

    query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s where id = %s'
    data = (first, last, company, cust_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    current_app.logger.info('GET /customers/<userID> route')
    cursor = db.get_db().cursor()
    cursor.execute('select id, first_name, last_name from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@customers.route('/customers/test', methods=['GET'])
def test_func():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM users;')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    response = make_response(jsonify(json_data))
    response.status_code = 200
    return response
