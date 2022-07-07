import service.compiler as compiler
from __init__ import *
import base64
import csv
from flask import request, jsonify, session

#-----------compilation part---------------------
@app.route('/compile/<problem_no>',  methods=["POST"])
def compile(problem_no):    

    print(request.get_json())
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404
    request_data = request.get_json()
    code = request_data['code']
    decoded = base64.b64decode(code).decode('utf-8')
    print(decoded)
    print(problem_no)
    tests = compiler.execute(decoded, int(problem_no))
    user_from_db = users_collection.find_one({'username' : current_user})
    problems = user_from_db['problems']
    problems[str(problem_no)] = tests
    print(tests)
    score = int(tests['1']==True) + int(tests['2']==True) + int(tests['3']==True) + int(tests['4']==True)
    score *=25
    print(score)
    print(problems)
    users_collection.update_one({"username": current_user}, {"$set": { "problems": problems }})

    with open('scores.csv', 'a') as f:
        writer = csv.writer(f)
        data = [str(current_user), problem_no, score]
        writer.writerow(data)
    f.close()
    return jsonify({'tests' : tests, 'user' : current_user }), 200
