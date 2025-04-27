from flask import Blueprint, jsonify
from app.models import Client, Program
from flask import request

# Define the Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api')

#Fetch a Single Client's Profile
@api_bp.route('/client/<int:client_id>', methods=['GET'])
def get_client_profile(client_id):
    client = Client.query.get_or_404(client_id)
    # Prepare client data in dictionary format
    client_data = {
        'id': client.id,
        'name': client.name,
        'age': client.age,
        'phone': client.phone,
        'email': client.email,
        'programs': [program.name for program in client.programs]  # List of programs the client is enrolled in
    }
    return jsonify(client_data), 200  # Return client data as JSON response

# Fetch All Clients (Optional, for admin use or external systems)
@api_bp.route('/clients', methods=['GET'])
def get_all_clients():
    clients = Client.query.all()
    clients_list = []
    for client in clients:
        client_data = {
            'id': client.id,
            'name': client.name,
            'age': client.age,
            'phone': client.phone,
            'email': client.email,
            'programs': [program.name for program in client.programs]  # List of programs the client is enrolled in
        }
        clients_list.append(client_data)
    return jsonify(clients_list), 200  # Return a list of clients in JSON format

