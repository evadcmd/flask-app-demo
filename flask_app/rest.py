from flask_restful import Resource
from flask_app.core import db
from flask_app import model

class HelloWorld(Resource):
    URL = '/'
    def get(self):
        return {'Hello': 'World!'}

class User(Resource):
    URL = '/api/user'
    def get(self):
        return model.User.query.all()

