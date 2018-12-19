import os
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config import Config

app = Flask(__name__, static_url_path="/public", static_folder="public")
CORS(app)
app.config.from_object(Config)
mdb = MongoEngine(app)

from app import models
from app.jsonSerializer import Encoder
from app.routes import test_routes, admin_routes, api_routes, auth_routes

app.json_encoder = Encoder

port = int(os.getenv("PORT") or 8888)
print(port)

if __name__ == '__main__':
    print('running on main')
else:
    print('running on', __name__)

app.run(host='0.0.0.0', port=port)