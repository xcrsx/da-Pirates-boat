from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from webapp.user.views import blueprint as user_blueprint
from webapp.search.views import blueprint as search_blueprint
from webapp.models import db
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint)
app.register_blueprint(search_blueprint)
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'user.login'
login = LoginManager(app)
login.login_view = 'user.login'
bootstrap = Bootstrap(app)

from webapp import routes
