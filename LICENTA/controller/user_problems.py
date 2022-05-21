from __init__ import *
import base64
import json
import hashlib
import datetime
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient

@app.route("/get_problems", methods=["GET"])
@jwt_required()
def get_problems():
    current_user = get_jwt_identity() # Get the identity of the current 
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if  not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404

    problems = user_from_db['problems']
    
    return jsonify({'msg': problems}), 200


@app.route("/get_problem_tests/<problem_no>", methods=["GET"])
@jwt_required()
def get_problem_tests(problem_no):
    current_user = get_jwt_identity() # Get the identity of the current 
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if  not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404

    problems = user_from_db['problems']
    if str(problem_no) not in problems:
        return jsonify({'msg': 'Problem not found'}), 406

    return jsonify({'msg': problems[str(problem_no)]}), 200

@app.route("/get_problem_score/<problem_no>", methods=["GET"])
@jwt_required()
def get_problem_scoare(problem_no):
    current_user = get_jwt_identity() # Get the identity of the current 
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if  not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404

    problems = user_from_db['problems']
    if str(problem_no) not in problems:
        return jsonify({'msg': 'Problem not found'}), 406

    current_problem = problems[str(problem_no)]

    score = 0
    for i in range(1,5):
        print(current_problem[str(i)])
        if current_problem[str(i)] == 200:
            score+=25

    return jsonify({'msg': score}), 200
