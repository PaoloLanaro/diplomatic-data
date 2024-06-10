from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.ml_models.Linear_Perceptron import predict, train
from backend.db_connection import db

utils = Blueprint('utils', __name__)

@utils.route('/countries/sorted_list', methods=['GET'])
def get_all_countries_sorted():
    current_app.logger.info('country routes: GET utils/countries/sorted_list')
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

@utils.route('/countries/unsorted_list', methods=['GET'])
def get_all_countries_unsorted():
    current_app.logger.info('country routes: GET utils/countries/unsorted_list')
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

@utils.route('/countries/codes', methods=['GET'])
def get_all_country_codes():
    cursor = db.get_db().cursor()
    # Get a cursor to all the country names from the country table
    query = 'SELECT country_code FROM country'
    cursor.execute(query)
    
    # Get the mapping from 'country_name' to each country's string
    country_names = cursor.fetchall()
    
    response = make_response(country_names)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response

@utils.route('/coordinates', methods=['GET'])
def get_country_coordinates(): 
    current_app.logger.info('GET /coordinates route')
    cursor = db.get_db().cursor()
    query = 'SELECT latitude, longitude FROM city_coordinates'
    cursor.execute(query)
    current_app.logger.info(f'coordinate query: {query}')

    latitude_longitude = cursor.fetchall()
    current_app.logger.info(f'lat and long: {latitude_longitude}')

    response = make_response(latitude_longitude)
    response.status_code = 200
    response.mimetype = 'application/json'
    return response
