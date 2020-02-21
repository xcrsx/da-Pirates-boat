from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from webapp.parsing.views import blueprint as parsing_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.user.models import User
from webapp.search.views import blueprint as search_blueprint
from webapp.db import db
from flask_bootstrap import Bootstrap

import os, logging
logging.basicConfig(filename=os.path.join(os.path.abspath(__name__), "logs.log"),
                    format='[%(levelname)s]: %(asctime)s [%(module)s > %(funcName)s > %(lineno)d]: %(message)s ',
                    datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)    
    migrate = Migrate(app, db)

    login = LoginManager(app)
    login.login_view = 'user.login'

    bootstrap = Bootstrap(app)

    app.register_blueprint(parsing_blueprint)
    app.register_blueprint(search_blueprint)
    app.register_blueprint(user_blueprint)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app