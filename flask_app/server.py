from flask_app.core import app
from flask_restful import Api

from flask_app import rest
from flask_app.config import server

api = Api(app, server['context-path'])
api.add_resource(rest.HelloWorld, rest.HelloWorld.URL)
api.add_resource(rest.User, rest.User.URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)