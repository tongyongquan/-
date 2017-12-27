#encoding: utf-8
from exts import db




class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    title = db.Column(db.String(30),nullable=False)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    password = db.Column(db.String(100),nullable=False)
    username = db.Column(db.String(50),nullable=False)