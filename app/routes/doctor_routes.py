from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Program, Client, Enrollment
from app.forms import ProgramForm, ClientForm  # Assuming you have these forms for creating programs and clients
from functools import wraps

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctor')

# Ensure only logged-in doctors can access these routes
def doctor_required(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.is_admin:
            flash("Unauthorized access.", "danger")
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return wrapper

# 1. Doctor's Dashboard (View Programs and Clients)
@doctor_bp.route('/dashboard')
@doctor_required
def dashboard():
    programs = Program.query.all()  # Fetch all programs
    clients = Client.query.all()  # Fetch all clients
    return render_template('doctor_dashboard.html', programs=programs, clients=clients)

# 2. Create a new Health Program
@doctor_bp.route('/program/create', methods=['GET', 'POST'])
@doctor_required
def create_program():
    form = ProgramForm()  # WTForm for creating programs
    if form.validate_on_submit():
        new_program = Program(
            name=form.name.data,
            description=form.description.data,
            created_by=current_user.id  # Created by the logged-in doctor
        )
        db.session.add(new_program)
        db.session.commit()
        flash("Health program created successfully!", "success")
        return redirect(url_for('doctor.dashboard'))  # Redirect back to dashboard
    return render_template('create_program.html', form=form)

# 3. Register a New Client
@doctor_bp.route('/client/register', methods=['GET', 'POST'])
@doctor_required
def register_client():
    form = ClientForm()  # WTForm for registering clients
    if form.validate_on_submit():
        new_client = Client(
            name=form.name.data,
            age=form.age.data,
            phone=form.phone.data,
            email=form.email.data,
            assigned_doctor=current_user.id  # Assign this client to the logged-in doctor
        )
        db.session.add(new_client)
        db.session.commit()
        flash("Client registered successfully!", "success")
        return redirect(url_for('doctor.dashboard'))  # Redirect to dashboard
    return render_template('register_client.html', form=form)

# 4. Enroll a Client in a Program
@doctor_bp.route('/client/enroll/<int:client_id>', methods=['GET', 'POST'])
@doctor_required
def enroll_client(client_id):
    client = Client.query.get_or_404(client_id)  # Fetch the client by ID
    programs = Program.query.all()  # Fetch all available programs
    if request.method == 'POST':
        selected_programs = request.form.getlist('program_ids')  # List of selected programs
        for program_id in selected_programs:
            program = Program.query.get(int(program_id))
            if program and program not in client.programs:
                client.programs.append(program)  # Enroll client in the program
        db.session.commit()
        flash("Client enrolled in the selected programs!", "success")
        return redirect(url_for('doctor.view_client', client_id=client.id))  # Redirect to client's profile
    return render_template('enroll_client.html', client=client, programs=programs)

# 5. View a Specific Client's Profile
@doctor_bp.route('/client/profile/<int:client_id>')
@doctor_required
def view_client(client_id):
    client = Client.query.get_or_404(client_id)  # Fetch the client by ID
    return render_template('client_profile.html', client=client)

# 6. View All Clients
@doctor_bp.route('/clients')
@doctor_required
def view_all_clients():
    clients = Client.query.all()  # Fetch all clients
    return render_template('clients_list.html', clients=clients)  # Removed the extra closing parenthesis
