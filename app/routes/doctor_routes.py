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
    form.type_id.choices = [(pt.id, pt.name) for pt in ProgramType.query.all()]

    if form.validate_on_submit():
        new_program = Program(
            title=form.name.data,
            description=form.description.data,
            type_id=form.type_id.data
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
            full_name=full_name,
            gender=form.gender.data,
            date_of_birth=form.date_of_birth.data,
            national_id=form.national_id.data,
            birth_certificate=form.birth_certificate.data,
            country=form.country.data,
            county=form.county.data,
            subcounty=form.subcounty.data,
            village=form.village.data,
            contact_number=form.contact_number.data,
            address=form.address.data,
            created_by=current_user.id
        )
        db.session.add(new_client)
        db.session.commit()
        flash("Client registered successfully!", "success")
        return redirect(url_for('doctor.dashboard'))
    return render_template('register_client.html', form=form)

# 4. Enroll a Client in a Program
@doctor_bp.route('/client/enroll', methods=['GET', 'POST'])
@doctor_required
def enroll_client():
    programs = Program.query.all()  # Fetch all available programs
    program_types = ProgramType.query.all()  # Fetch all program types

    if request.method == 'POST':
        client_name = request.form.get('client_name')
        admission_number = request.form.get('admission_number')
        program_id = request.form.get('program_id')
        program_type_id = request.form.get('program_type')

        # Fetch the program and program type
        program = Program.query.get(program_id)
        program_type = ProgramType.query.get(program_type_id)

        # Add the new enrollment (assuming the Enrollment model is linked to client and program)
        new_enrollment = Enrollment(
            client_name=client_name,
            admission_number=admission_number,
            program_id=program.id,
            program_type_id=program_type.id
        )
        db.session.add(new_enrollment)
        db.session.commit()

        flash("Client enrolled successfully!", "success")
        return redirect(url_for('doctor.dashboard'))

    return render_template(
        'enroll_client.html',  # Your template name
        programs=programs,
        program_types=program_types
    )


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
