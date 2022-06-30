from flask import Flask
import datetime
from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
cors = CORS(app, origins=CORS_ALLOW_ORIGIN.split(","), allow_headers=CORS_ALLOW_HEADERS.split(",") , expose_headers= CORS_EXPOSE_HEADERS.split(","),   supports_credentials = True)

app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
app.secret_key = 'secret key'
client = MongoClient("mongodb+srv://ioanstanciu:anaaremere@cluster0.9wluw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") # your connection string
db = client["users"]
users_collection = db["users"]