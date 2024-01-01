from flask_sqlalchemy import SQLAlchemy
from flask import Flask,url_for, request, redirect
db = SQLAlchemy()


class Post(db.Model):
    # __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)   #.column because sqlalchemy
    name=db.Column(db.String)
    image=db.Column(db.String)
    body = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())
    
    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
    
    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_post(cls, request_form):
        std = cls(**request_form)
        db.session.add(std)
        db.session.commit()
        return std
    
    @classmethod
    def get_specific_post(cls, id):
        return  cls.query.get_or_404(id)

    @property
    def get_image_url(self):
        return url_for('static', filename=f'posts/images/{self.image}')


    @property
    def get_show_url(self):
        return  url_for('posts.show', id=self.id)

class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())
    posts= db.relationship('Post', backref='category_name', lazy=True)

    def __str__(self):
        return f"{self.name}"
    
    
    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_category(cls, request_form):
        ctg = cls(**request_form)
        db.session.add(ctg)
        db.session.commit()
        return ctg
    
    @classmethod
    def get_specific_category(cls, id):
        return  cls.query.get_or_404(id)
