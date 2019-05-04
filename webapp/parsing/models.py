from webapp.db import db


class SoundCloud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=True)
    art = db.Column(db.String, nullable=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    music_url = db.Column(db.String)
    date_entry = db.Column(db.DateTime)  

    def __repr__(self):
        return '<New on SoundCloud {} {} {} {} {} {}'.format(self.genre, 
                                                            self.art,
                                                            self.author, 
                                                            self.title, 
                                                            self.music_url, 
                                                            self.date_entry)



class Bandcamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=True)
    art = db.Column(db.String, nullable=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    music_url = db.Column(db.String)
    date_entry = db.Column(db.DateTime) 

    def __repr__(self):
        return '<New on Bandcamp {} {} {} {} {} {}'.format(self.genre, 
                                                            self.art,
                                                            self.author, 
                                                            self.title, 
                                                            self.music_url, 
                                                            self.date_entry)
