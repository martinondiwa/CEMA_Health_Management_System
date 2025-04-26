from app import db
from app import create_app  # if you're using an app factory
from app.models import *    # optional, to ensure all models are loaded

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database tables dropped and recreated.")
