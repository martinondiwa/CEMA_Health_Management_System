from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Doctor  # Ensure that Doctor model is imported if not already
from app.extensions import db
from app.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

# Create the Blueprint for the authentication routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 1. Login Route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('doctor.dashboard')) # Redirect to doctor dashboard if already logged in

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Check if the email exists
        if user and check_password_hash(user.password_hash, form.password.data):  # Use password_hash instead of password
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('doctor.dashboard'))  # Redirect to doctor dashboard after successful login
        else:
            flash('Invalid login credentials. Please try again.', 'danger')
    return render_template('auth/login.html', form=form)

# 2. Register Route (for doctor/admin only)
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('auth.login'))

        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        new_user = User(
            email=form.email.data,
            password_hash=hashed_password,
            is_admin=form.is_admin.data
        )
        db.session.add(new_user)
        db.session.commit()

        new_doctor = Doctor(
            user_id=new_user.id,
            full_name=form.name.data,
            phone=form.phone.data,
            department=form.department.data
        )
        db.session.add(new_doctor)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login')) 

    return render_template('auth/register.html', form=form)

# 3. Logout Route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Log the current user out
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
