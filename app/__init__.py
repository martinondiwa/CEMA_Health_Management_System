# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config

# Extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Import models so migrations can detect them
    from app import models

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.client_routes import client_bp
    from app.routes.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
