from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Goods(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
