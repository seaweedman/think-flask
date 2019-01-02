from api import create_app
from db import db

app = create_app()

db.init_app(app)
db.create_all(app=app)

if __name__ == '__main__':
    app.run()