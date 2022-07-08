from flask import request, session
from __init__ import *
import hashlib
from flask import request, jsonify
import service.user_management as user_management
#-----------user management--------------------------

@app.route("/register", methods=["POST"])
def register():
    new_user = request.get_json() 
    return user_management.register(new_user)

@app.route("/login", methods=["POST"])
def login():
    login_details = request.get_json() 
    return user_management.login(login_details)

@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("username")
    return "200"

@app.route("/user", methods=["GET"])
def profile():
    return user_management.user()

