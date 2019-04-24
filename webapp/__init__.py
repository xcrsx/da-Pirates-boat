from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from webapp.db import db


migrate = Migrate()
login_ = LoginManager()
login_.login_view = 'user.login'
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_.init_app(app)
    bootstrap.init_app(app)

    from webapp.parsing.views import blueprint as parsing_blueprint
    app.register_blueprint(parsing_blueprint)

    from webapp.search.views import blueprint as search_blueprint
    app.register_blueprint(search_blueprint)

    from webapp.user.views import blueprint as user_blueprint
    app.register_blueprint(user_blueprint)

    from webapp.user.models import User
    @login_.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
