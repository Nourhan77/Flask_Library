from flask import Flask
from .config import Config
from iti.models import db




def create_app ():
    app =Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    from .Books.views import books_blueprint
    app.register_blueprint(books_blueprint)

    from .Author.views import authors_blueprint
    app.register_blueprint(authors_blueprint)



    return app