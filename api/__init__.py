from flask import Flask, Blueprint
from flask_restful import Api

def create_app():
    app = Flask(__name__)

    from api.v1 import create_resource_v1

    blueprint_v1 = Blueprint('api_v1', __name__)
    api_v1 = Api(blueprint_v1)
    create_resource_v1(api_v1)
    app.register_blueprint(blueprint_v1, url_prefix='/v1')

    return app