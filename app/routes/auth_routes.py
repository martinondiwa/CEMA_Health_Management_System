from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db
from app.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

# Create the Blueprint for the authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 1. Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('doctor.view_dashboard'))  # Redirect to doctor dashboard if already logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Check if the email exists
        if user and check_password_hash(user.password, form.password.data):  # Validate password
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('doctor.view_dashboard'))  # Redirect to doctor dashboard after successful login
        else:
            flash('Invalid login credentials. Please try again.', 'danger')
    return render_template('auth/login.html', form=form)

# 2. Register Route (for doctor/admin only)
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('doctor.view_dashboard'))  # Redirect to dashboard if already logged in

    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'danger')
            return redirect(url_for('auth.register'))  # Redirect back to registration form if email exists

        # Create a new user (doctor/admin)
        hashed_password = generate_password_hash(form.password.data, method='sha256')  # Hash password before storing
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            role='doctor' if form.role.data == 'doctor' else 'admin'  # Role selection (doctor or admin)
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('auth.login'))  # Redirect to login page after successful registration
    return render_template('auth/register.html', form=form)

# 3. Logout Route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Log the current user out
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))  # Redirect to login page after logout

