import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_app.config import server, database

app = Flask(__name__)

# settings for docker
database_ip = 'db' if os.environ.get('IN_CONTAINER', False) else server['ip']

app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=f'{database["type"]}://{database["username"]}:{database["password"]}@{database_ip}:{database["port"]}/{database["dbname"]}',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    APPLICATION_ROOT=server['context-path']
)

db = SQLAlchemy(app)