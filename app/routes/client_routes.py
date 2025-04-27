# app/routes/client_routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Client, Program
from app import db

# Define the Blueprint for client-related routes
client_bp = Blueprint('client', __name__)

# Route to view a client's profile
@client_bp.route('/profile/<int:client_id>', methods=['GET'])
def view_profile(client_id):
    client = Client.query.get_or_404(client_id)
    # Fetch the programs the client is enrolled in
    enrolled_programs = client.programs
    return render_template('client_profile.html', client=client, programs=enrolled_programs)


