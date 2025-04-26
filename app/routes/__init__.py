# app/routes/__init__.py

from flask import Blueprint

# Import each blueprint from their respective modules
from app.routes.auth_routes import auth_bp
from app.routes.doctor_routes import doctor_bp
from app.routes.client_routes import client_bp
from app.routes.api import api_bp

# Function to register all Blueprints
def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(doctor_bp, url_prefix='/doctor')
    app.register_blueprint(client_bp, url_prefix='/client')
    app.register_blueprint(api_bp, url_prefix='/api')
