from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


favorite_songs = db.Table('favorite_song',
                          db.Column('favorite_id', db.Integer,
                                    db.ForeignKey('user.id')),
                          db.Column('url', db.String, unique=True))


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Favorite {}>'.format(self.artist)


class Popular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String, nullable=True)
    pic = db.Column(db.String, nullable=True)
    url = db.Column(db.String)    

    def __repr__(self):
        return '<New on SoundCloud {} {} {} {}'.format(self.title, self.genre, self.pic, self.url)


class Bandcamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_text = db.Column(db.String, nullable=True)
    art_id = db.Column(db.String, nullable=True)
    primary_text = db.Column(db.String)
    secondary_text = db.Column(db.String)
    title = db.Column(db.String)
    file = db.Column(db.String) 

    def __repr__(self):
        return '<New on Bandcamp {} {} {} {} {} {}'.format(self.genre_text, 
                                                            self.art_id, self.primary_text, 
                                                            self.secondary_text, 
                                                            self.title, self.file)