from flask_restful import Resource

class Goods(Resource):
    def get(self):
        return {'id': 1, 'name': 'egg'}

    def post(self):
        pass