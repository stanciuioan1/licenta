import numpy as np
import pandas as pd
import time
from __init__ import *
import math
import numpy
from flask import request, session
import hashlib
from flask import request, jsonify
import service.user_management as user_management


def login(login_details):
    user_from_db = users_collection.find_one({'username': login_details['username']})  
    encrpted_password = ''
    if user_from_db is None:
        response = jsonify({'msg': 'The username or password is incorrect'}), 401

        return response
    if user_from_db:
        encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
    if encrpted_password == user_from_db['password']:
        session['username'] = login_details['username']
        response = jsonify(username=login_details['username']), 200
        return response

    response = jsonify({'msg': 'The username or password is incorrect'}), 401
    return response

def register(new_user):
    new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() 
    doc = users_collection.find_one({"username": new_user["username"]}) 
    if not doc:
        new_user["problems"] = {}
        users_collection.insert_one(new_user)
        return jsonify({'msg': 'User created successfully'}), 201
    else:
         jsonify({'msg': 'Username already exists'}), 409

def user():
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    user_from_db = users_collection.find_one({'username' : current_user})
    if user_from_db:
        del user_from_db['_id'], user_from_db['password']
        return jsonify({'profile' : user_from_db }), 200
    else:
        return jsonify({'msg': 'Profile not found'}), 404
