from webapp.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String, nullable=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return self.song


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    favorite = db.relationship('Favorite', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_to_favorite(self, song):
        if not self.is_favorite(song):
            self.favorite.append(song)

    def remove_from_favorite(self, song):
        if self.is_favorite(song):
            self.favorite.remove(song)

    def is_favorite(self, song):
        return self.favorite.filter(Favorite.song == song).count() > 0

    
