from flask import Blueprint, request, jsonify, make_response, current_app
import json 
from backend.db_connection import db

users = Blueprint('users', __name__)

@users.route('/asdf', methods=['GET'])
def ljaksf():
    data = {              
                "user1": {
                    "Name": "Mark Fontenot",
                    "Course": "CS 3200",
                },
                "user2": {
                    "Name": "Eric Gerber",
                    "Course": "DS 3000",
                }
            }
    return data
    # cursor = db.get_db().cursor()
    # cursor.execute('SELECT id, product_code, product_name, list_price, category FROM products')

@users.route('')
