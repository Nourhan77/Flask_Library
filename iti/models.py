from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, SelectField

db=SQLAlchemy()


class Book(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    description = db.Column(db.String(120),nullable=True,default="default.png")
    image = db.Column(db.String(120),nullable=False,)
    price=db.Column(db.Float,nullable=False)
    appropriate=db.Column(db.String(120), nullable=False)
    author_id=db.Column(db.ForeignKey('authors.id'))

class Author(db.Model):
    __tablename__="authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    books=db.relationship('Book',backref='auhtor',lazy=True)

