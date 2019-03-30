import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SC_API_MAINPAGE = "https://api-v2.soundcloud.com/featured_tracks/front?client_id=z7npDMrLmgiW4wc8pPCQkkUUtRQkWZOF&limit=20&offset=0&linked_partitioning=1&app_version=1553260698&app_locale=en"
