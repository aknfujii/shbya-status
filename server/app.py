from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)
SQLALCHEMY_DATABASE_URI = "sqlite:///models.db"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["DEBUG"] = True
ma = Marshmallow(app)
db = SQLAlchemy(app)

from views import *
