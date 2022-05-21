from flask import request, session

from __init__ import *

import hashlib

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


#-----------user management--------------------------

@app.route("/register", methods=["POST"])
def register():
    new_user = request.get_json() # store the json body request
    new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
    doc = users_collection.find_one({"username": new_user["username"]}) # check if user exist
    if not doc:
        new_user["problems"] = []
        users_collection.insert_one(new_user)
        return jsonify({'msg': 'User created successfully'}), 201
    else:
         jsonify({'msg': 'Username already exists'}), 409

@app.route("/login", methods=["POST"])
def login():
    login_details = request.get_json() # store the json body request
    user_from_db = users_collection.find_one({'username': login_details['username']})  # search for user in database

    if user_from_db:
        encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
    if encrpted_password == user_from_db['password']:
        access_token = create_access_token(identity=user_from_db['username']) # create jwt 
        session['access_token'] = access_token
        return jsonify(access_token=access_token), 200

    return jsonify({'msg': 'The username or password is incorrect'}), 401


@app.route("/user", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity() # Get the identity of the current 
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if user_from_db:
        del user_from_db['_id'], user_from_db['password'] # delete data we don't want to return
        return jsonify({'profile' : user_from_db }), 200
    else:
        return jsonify({'msg': 'Profile not found'}), 404
    #return jsonify(access_token=access_token), 200
