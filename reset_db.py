from app import db
from app import create_app  
from app.models import *    #  ensures all models are loaded

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database tables dropped and recreated.")
