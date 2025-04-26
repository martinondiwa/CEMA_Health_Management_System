from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Program, Client, Enrollment
from app.forms import ProgramForm, ClientForm  # Assuming these exist in forms.py

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctor')

# Ensure only logged-in doctors can access these routes
def doctor_required(func):
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.role != 'doctor':
            flash("Unauthorized access.", "danger")
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@doctor_bp.route('/dashboard')
@doctor_required
def dashboard():
    programs = Program.query.filter_by(created_by=current_user.id).all()
    clients = Client.query.filter_by(assigned_doctor=current_user.id).all()
    return render_template('doctor_dashboard.html', programs=programs, clients=clients)

@doctor_bp.route('/create_program', methods=['GET', 'POST'])
@doctor_required
def create_program():
    form = ProgramForm()
    if form.validate_on_submit():
        new_program = Program(
            name=form.name.data,
            description=form.description.data,
            created_by=current_user.id
        )
        db.session.add(new_program)
        db.session.commit()
        flash("Program created successfully!", "success")
        return redirect(url_for('doctor.dashboard'))
    return render_template('create_program.html', form=form)

@doctor_bp.route('/register_client', methods=['GET', 'POST'])
@doctor_required
def register_client():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            assigned_doctor=current_user.id
        )
        db.session.add(client)
        db.session.commit()
        flash("Client registered successfully.", "success")
        return redirect(url_for('doctor.dashboard'))
    return render_template('register_client.html', form=form)

@doctor_bp.route('/clients')
@doctor_required
def view_clients():
    clients = Client.query.filter_by(assigned_doctor=current_user.id).all()
    return render_template('clients_list.html', clients=clients)
