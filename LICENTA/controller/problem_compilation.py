from flask import Flask, request, session
import compiler
from __init__ import *
import base64

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity







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
