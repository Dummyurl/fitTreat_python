from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__, static_url_path="/public", static_folder="public")

app.config.from_object(Config)
mdb = MongoEngine(app)

from app import routes, models
from app.jsonSerializer import Encoder

app.json_encoder = Encoder
