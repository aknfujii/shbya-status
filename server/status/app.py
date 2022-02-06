from flask import Flask
from flask_cors import CORS
from datetime import timezone,timedelta

app = Flask(__name__)
app.config['TIMEZONE'] = timezone(timedelta(hours=+9), "JST")
CORS(app)

from .api import *
