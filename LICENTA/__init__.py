from flask import Flask
import datetime
from flask import Flask
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from flask import Flask, request, session

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.secret_key = 'secret key'
client = MongoClient("mongodb+srv://ioanstanciu:anaaremere@cluster0.9wluw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # your connection string
db = client["users"]
users_collection = db["users"]