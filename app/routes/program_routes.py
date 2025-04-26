from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import db, Program
from app.forms import ProgramForm  # Assuming you have a WTForm for creating and updating programs

program_bp = Blueprint('program', __name__, url_prefix='/program')

# Ensure only logged-in doctors/admins can access these routes
def doctor_required(func):
    @login_required
    def wrapper(*args, **kwargs):
        if current_user.role != 'doctor' and current_user.role != 'admin':  # Ensure the user is a doctor/admin
            flash("Unauthorized access.", "danger")
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# 1. Create a Health Program
@program_bp.route('/create', methods=['GET', 'POST'])
@doctor_required
def create_program():
    form = ProgramForm()  # WTForm for creating programs
    if form.validate_on_submit():
        new_program = Program(
            name=form.name.data,
            description=form.description.data,
            created_by=current_user.id  # Created by the logged-in doctor/admin
        )
        db.session.add(new_program)
        db.session.commit()
        flash("Health program created successfully!", "success")
        return redirect(url_for('program.view_all_programs'))  # Redirect to program list
    return render_template('create_program.html', form=form)

# 2. View All Programs
@program_bp.route('/', methods=['GET'])
@doctor_required
def view_all_programs():
    programs = Program.query.all()  # Fetch all health programs
    return render_template('view_programs.html', programs=programs)

# 3. View a Specific Program
@program_bp.route('/<int:program_id>', methods=['GET'])
@doctor_required
def view_program(program_id):
    program = Program.query.get_or_404(program_id)  # Fetch the program by ID
    return render_template('view_program.html', program=program)

# 4. Update a Program
@program_bp.route('/update/<int:program_id>', methods=['GET', 'POST'])
@doctor_required
def update_program(program_id):
    program = Program.query.get_or_404(program_id)  # Fetch the program by ID
    form = ProgramForm(obj=program)  # Pre-populate the form with current program data
    if form.validate_on_submit():
        program.name = form.name.data
        program.description = form.description.data
        db.session.commit()
        flash("Health program updated successfully!", "success")
        return redirect(url_for('program.view_program', program_id=program.id))  # Redirect to the program details
    return render_template('update_program.html', form=form, program=program)

# 5. Delete a Program
@program_bp.route('/delete/<int:program_id>', methods=['POST'])
@doctor_required
def delete_program(program_id):
    program = Program.query.get_or_404(program_id)  # Fetch the program by ID
    db.session.delete(program)
    db.session.commit()
    flash("Health program deleted successfully!", "success")
    return redirect(url_for('program.view_all_programs'))  # Redirect to the program list
