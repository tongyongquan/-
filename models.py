#encoding: utf-8
from exts import db

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    title = db.Column(db.String(30),nullable=False)

