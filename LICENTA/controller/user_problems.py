from __init__ import *
from flask import jsonify
from flask import  session

@app.route("/get_problems", methods=["GET"])
def get_problems():
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if  not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404

    problems = user_from_db['problems']
    
    return jsonify({'msg': problems}), 200


@app.route("/get_problem_tests/<problem_no>", methods=["GET"])
def get_problem_tests(problem_no):
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    print(current_user)
    user_from_db = users_collection.find_one({'username' : current_user})
    if  not user_from_db:
        return jsonify({'msg': 'Profile not found'}), 404

    problems = user_from_db['problems']
    if str(problem_no) not in problems:
        return jsonify({'msg': 'Problem not found'}), 406

    return jsonify({'msg': problems[str(problem_no)]}), 200

@app.route("/get_problem_score/<problem_no>", methods=["GET"])
def get_problem_scoare(problem_no):
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
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
