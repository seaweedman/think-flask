from api.v1 import goods

def create_resource_v1(api):
    api.add_resource(goods.Goods, '/goods')