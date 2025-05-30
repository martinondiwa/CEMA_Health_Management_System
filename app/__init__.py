from flask import Flask
from config import Config

# Import extensions from the new module
from app.extensions import db, migrate, login_manager, bcrypt
from app.models import User

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Set login view and message category
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import models for migrations
    from app import models

    # Register blueprints AFTER extensions are initialized
    from app.routes.auth_routes import auth_bp
    from app.routes.doctor_routes import doctor_bp
    from app.routes.client_routes import client_bp
    from app.routes.api import api_bp
    from app.routes.index_routes import index_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(index_bp)

    return app  
