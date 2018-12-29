from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)

    from api.v1 import create_resource_v1

    create_resource_v1(Api(app))

    return app