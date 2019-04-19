from webapp.db import db


class SoundCloud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String, nullable=True)
    pic = db.Column(db.String, nullable=True)
    url = db.Column(db.String)    

    def __repr__(self):
        return '<New on SoundCloud {} {} {} {}'.format(self.title, self.genre, self.pic, self.url)


class Bandcamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=True)
    art = db.Column(db.String, nullable=True)
    album = db.Column(db.String)
    autor = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String) 

    def __repr__(self):
        return '<New on Bandcamp {} {} {} {} {} {}'.format(self.genre_text, 
                                                            self.art_id, self.primary_text, 
                                                            self.secondary_text, 
                                                            self.title, self.file)