from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Linear_Perceptron import predict, train
from backend.db_connection import db

country = Blueprint('country', __name__)

@country.route('/sorted_list', methods=['GET'])
def get_all_countries_sorted():
    current_app.logger.info('country routes: GET /country/sorted_list')
    current_app.logger.info('This route should return all countries sorted lexicographically')
    
    # Establish a connection to the database
    cursor = db.get_db().cursor()
    # Get a cursor to all the country names from the country table
    query = 'SELECT country_name FROM country ORDER BY country_name'
    cursor.execute(query)
    
    # Get the mapping from 'country_name' to each country's string
    country_names = cursor.fetchall()

    # Make a success response to the request
    response = make_response(country_names)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response


@country.route('/unsorted_list', methods=['GET'])
def get_all_countries_unsorted():
    current_app.logger.info('country routes: GET /country/unsorted_list')
    current_app.logger.info('This route should return all countries unsorted')
    
    # Establish a connection to the database
    cursor = db.get_db().cursor()
    # Get a cursor to all the country names from the country table
    query = 'SELECT country_name FROM country'
    cursor.execute(query)
    
    # Get the mapping from 'country_name' to each country's string
    country_names = []
    country_names = cursor.fetchall()

    # Make a success response to the request
    response = make_response(country_names)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

