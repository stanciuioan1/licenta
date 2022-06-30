from flask import  session
from __init__ import *
from service.problem_recommeder import *
from flask import jsonify


@app.route('/get_content_based_recommendation/<problem_no>')
def content_based_recommendation(problem_no):
    current_user = session.get("username")
    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    x = Content_Based_Filtering()
    message =  x.get_available_problems(current_user, problem_no)
    return jsonify({'msg': message}), 201


@app.route('/get_collaborative_recommendation/<problem_no>')
def collaborative_recommendation(problem_no):
    current_user = session.get("username")
    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    x = Collaborative_Filtering()
    message =  x.collaborative_filtering(problem_no)
    return jsonify({'msg': message}), 201


@app.route('/get_my_collaborative_recommendation/<problem_no>')
def my_collaborative_recommendation(problem_no):
    current_user = session.get("username")
    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    x = My_Collaborative_Filtering()
    message =  x.compute_knn(problem_no)
    return jsonify({'msg': message}), 201