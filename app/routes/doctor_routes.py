from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Program, Client, Enrollment
from app.forms import ProgramForm, ClientRegistrationForm, EnrollmentForm
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


# 1. Doctor's Dashboard
@doctor_bp.route('/dashboard')
@doctor_required
def dashboard():
    programs = Program.query.all()
    clients = Client.query.all()
    program_form = ProgramForm()
    client_form = ClientRegistrationForm()
    enrollment_form = EnrollmentForm()

    return render_template(
        'doctor_dashboard.html',
        programs=programs,
        clients=clients,
        program_form=program_form,
        client_form=client_form,
        enrollment_form=enrollment_form
    )


# 2. Create a new Health Program
@doctor_bp.route('/program/create', methods=['GET', 'POST'])
@doctor_required
def create_program():
    form = ProgramForm()
    if form.validate_on_submit():
        new_program = Program(
            title=form.name.data,  # ❗ 'title' instead of 'name' (models.py uses `title`)
            description=form.description.data
        )
        db.session.add(new_program)
        db.session.commit()
        flash("Health program created successfully!", "success")
        return redirect(url_for('doctor.dashboard'))
    return render_template('create_program.html', form=form)


# 3. Register a New Client
@doctor_bp.route('/client/register', methods=['GET', 'POST'])
@doctor_required
def register_client():
    form = ClientRegistrationForm()
    if form.validate_on_submit():
        full_name = " ".join(filter(None, [form.first_name.data, form.middle_name.data, form.sir_name.data]))
        new_client = Client(
            full_name=full_name,  # ✅ Corrected from 'name' to 'full_name'
            gender=form.gender.data,
            date_of_birth=form.date_of_birth.data,
            contact_number=form.contact_number.data,
            address=form.address.data,
            created_by=current_user.id  # ✅ This maps to 'created_by' in Client model
        )
        db.session.add(new_client)
        db.session.commit()
        flash("Client registered successfully!", "success")
        return redirect(url_for('doctor.dashboard'))
    return render_template('register_client.html', form=form)


# 4. Enroll a Client in a Program
@doctor_bp.route('/client/enroll/<int:client_id>', methods=['GET', 'POST'])
@doctor_required
def enroll_client(client_id):
    client = Client.query.get_or_404(client_id)
    programs = Program.query.all()
    if request.method == 'POST':
        selected_programs = request.form.getlist('program_ids')
        for program_id in selected_programs:
            program = Program.query.get(int(program_id))
            if program and program not in client.programs:
                client.programs.append(program)
        db.session.commit()
        flash("Client enrolled in the selected programs!", "success")
        return redirect(url_for('doctor.view_client', client_id=client.id))
    return render_template('enroll_client.html', client=client, programs=programs)


# 5. View a Specific Client's Profile
@doctor_bp.route('/client/profile/<int:client_id>')
@doctor_required
def view_client(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template('client_profile.html', client=client)


# 6. View All Clients
@doctor_bp.route('/clients')
@doctor_required
def view_all_clients():
    clients = Client.query.all()
    return render_template('clients_list.html', clients=clients)


# 7. Search for a Client
@doctor_bp.route('/client/search', methods=['GET'])
@doctor_required
def search_client():
    query = request.args.get('query')
    if query:
        clients = Client.query.filter(
            (Client.full_name.ilike(f'%{query}%')) | (Client.id.ilike(f'%{query}%'))  # ✅ Corrected 'name' to 'full_name'
        ).all()
    else:
        clients = []
    return render_template('search_results.html', clients=clients, query=query)
