from flask import Flask
from config import Config

# Import extensions from the new module
from app.extensions import db, migrate, login_manager, bcrypt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Import models for migrations
    from app import models

    # Register blueprints AFTER extensions are initialized
    from app.routes.auth_routes import auth_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.client_routes import client_bp
    from app.routes.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
