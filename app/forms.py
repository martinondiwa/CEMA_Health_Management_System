# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

# Login form (shared by doctors/admins)
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

# Registration form for doctors/admins (only admin can access)
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    department = StringField('Department')
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('Register as Admin')  # Optional toggle
    submit = SubmitField('Register')

# Form to register a client
class ClientRegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    middle_name = StringField("Middle Name", validators=[Optional(), Length(max=50)])
    sir_name = StringField("Sir Name", validators=[DataRequired(), Length(max=50)])

    date_of_birth = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    
    gender = SelectField("Gender", choices=[
        ('Male', 'Male'), 
        ('Female', 'Female'), 
        ('Other', 'Other')
    ], validators=[DataRequired()])

    national_id = StringField("National ID", validators=[Optional(), Length(max=20)])
    birth_certificate = StringField("Birth Certificate Number", validators=[Optional(), Length(max=20)])

    country = StringField("Country", validators=[DataRequired(), Length(max=50)])
    county = StringField("County", validators=[DataRequired(), Length(max=50)])
    subcounty = StringField("Sub-county", validators=[DataRequired(), Length(max=50)])
    village = StringField("Village / Locality", validators=[DataRequired(), Length(max=100)])

    contact_number = StringField("Contact Number", validators=[DataRequired(), Length(max=100)])
    address = StringField("Address", validators=[Optional(), Length(max=200)])

    submit = SubmitField("Register Client")

# Form to create a health program
class ProgramForm(FlaskForm):
    title = StringField('Program Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Program')
class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
    
# Form to enroll client into a program
class EnrollmentForm(FlaskForm):
    client_id = IntegerField('Client ID', validators=[DataRequired()])
    program_id = IntegerField('Program ID', validators=[DataRequired()])
    submit = SubmitField('Enroll Client')
