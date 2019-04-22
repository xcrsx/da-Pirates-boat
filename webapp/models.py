from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String, nullable=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def is_favorite(self, song):
        return self.filter(Favorite.song == song).count() > 0

    def __repr__(self):
        return self.song


class Popular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String, nullable=True)
    pic = db.Column(db.String, nullable=True)
    url = db.Column(db.String)

    def __repr__(self):
        return '<New on SoundCloud {} {} {} {}'.format(self.title, self.genre, self.pic, self.url)