from webapp import app
from webapp.models import Favorite, db
from webapp.user.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Favorite': Favorite}
