# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Login form (shared by doctors/admins)
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

# Registration form for doctors/admins (only admin can access)
class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    department = StringField('Department')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('Register as Admin')  # Optional toggle
    submit = SubmitField('Register')

# Form to register a client
class ClientRegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    contact_number = StringField('Contact Number')
    address = StringField('Address')
    submit = SubmitField('Register Client')

# Form to create a health program
class ProgramForm(FlaskForm):
    title = StringField('Program Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Program')

# Form to enroll client into a program
class EnrollmentForm(FlaskForm):
    client_id = IntegerField('Client ID', validators=[DataRequired()])
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    submit = SubmitField('Enroll Client')
