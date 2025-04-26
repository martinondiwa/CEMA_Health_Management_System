# app/routes/index_routes.py

from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def home():
    return render_template('home.html')  # Or whatever your home template is
