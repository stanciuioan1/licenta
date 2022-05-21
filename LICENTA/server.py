from flask import Flask, request, session
import compiler
import problem_details
import problem_recommeder
from __init__ import *
import base64
import json
import hashlib
import datetime
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient








#-----------compilation part---------------------

@app.route('/compile/<problem_no>')
@jwt_required()
def compile(problem_no):
    current_user = get_jwt_identity() # Get the identity of the current 
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404
    request_data = request.get_json()
    code = request_data['code']
    #problem_no = request_data['problem_no']
    decoded = base64.b64decode(code).decode('utf-8')
    print(decoded)
    print(problem_no)
    tests = compiler.compile(decoded, int(problem_no))
    #users_collection.update_one({"username": current_user}, {"$set": { "problems": {} }})
    user_from_db = users_collection.find_one({'username' : current_user})
    problems = user_from_db['problems']
    print(problems)
    problems[str(problem_no)] = tests
    
    print(problems)
    users_collection.update_one({"username": current_user}, {"$set": { "problems": problems }})
    #return tests
    #problems = user_from_db['problems']
    #problems[str(problem_no)] = str(tests)
    #user_from_db['problems'] = problems
    #users_collection.update_one({'username' : current_user}, user_from_db)
    return jsonify({'tests' : tests, 'user' : current_user }), 200

#---------problem_details------------------------

@app.route('/enunt/<problem_no>')
def get_enunt(problem_no):
    return problem_details.get_enunt(problem_no)


@app.route('/date_intrare/<problem_no>')
def get_date_intrare(problem_no):
    return problem_details.get_date_intrare(problem_no)


@app.route('/date_iesire/<problem_no>')
def get_date_iesire(problem_no):
    return problem_details.get_date_iesire(problem_no)

@app.route('/exemplu/<problem_no>')
def get_exemplu(problem_no):
    return problem_details.get_exemplu(problem_no)

@app.route('/tags/<problem_no>')
def get_tags(problem_no):
    return problem_details.get_tags(problem_no)

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

# main driver function
if __name__ == '__main__':
  
    app.run()