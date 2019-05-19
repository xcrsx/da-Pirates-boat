from webapp import create_app
from webapp.db import db
from webapp.user.models import User, Favorite


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Favorite': Favorite}
