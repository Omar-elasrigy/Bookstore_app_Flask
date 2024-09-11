from flask import Flask
from flask_migrate import Migrate
from app.config import productionConfig
from app.models import db
from app.book import landing_blueprint,book_blueprint
from flask_bootstrap import Bootstrap5


def create_app():
    app=Flask(__name__)
    app.config.from_object(productionConfig)
    db.init_app(app)
    migrate=Migrate(app,db)
    app.register_blueprint(landing_blueprint)
    app.register_blueprint(book_blueprint)
    bootstrap=Bootstrap5(app)

    return app


    
    


