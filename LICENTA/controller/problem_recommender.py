from flask import request, session

from __init__ import *
from service.problem_recommeder import *
import hashlib

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

@app.route('/get_content_based_recommendation/<problem_no>')
#@jwt_required()
def content_based_recommendation(problem_no):
    current_user = session.get("username")

    if not current_user:
        return jsonify({"error": "Unauthorized"}), 401
    #current_user = get_jwt_identity()

    x = Content_Based_Filtering()
    message =  x.get_available_problems(current_user, problem_no)
    return jsonify({'msg': message}), 201


@app.route('/get_collaborative_recommendation/<problem_no>')
#@jwt_required()
def collaborative_recommendation(problem_no):
    #current_user = get_jwt_identity()
    x = Collaborative_Filtering()
    message =  x.collaborative_filtering(problem_no)
    return jsonify({'msg': message}), 201