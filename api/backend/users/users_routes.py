from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

users = Blueprint('users', __name__)

@users.routes('', methods=['GET'])
def ljaksf():
   print("hello")






