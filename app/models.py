from app.extensions import db  
from flask_login import UserMixin
from datetime import datetime

# User model for authentication (admin/doctor login)
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # True for superadmin, False for doctors

    def __repr__(self):
        return f"<User {self.email}>"

# Doctor model for additional profile info
class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    department = db.Column(db.String(100), nullable=True)

    user = db.relationship('User', backref=db.backref('doctor_profile', uselist=False))

    def __repr__(self):
        return f"<Doctor {self.full_name}>"

# Client model (added by doctors)
class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

    national_id = db.Column(db.String(20), nullable=True)
    birth_certificate = db.Column(db.String(20), nullable=True)

    country = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    subcounty = db.Column(db.String(50), nullable=False)
    village = db.Column(db.String(100), nullable=False)

    contact_number = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=True)

    created_by = db.Column(db.Integer, db.ForeignKey('doctors.id'))  # doctor who registered

    doctor = db.relationship('Doctor', backref='clients')

    def __repr__(self):
        return f"<Client {self.full_name}>"

# ProgramType model
class ProgramType(db.Model):
    __tablename__ = 'program_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    programs = db.relationship('Program', back_populates='program_type')
    enrollments = db.relationship('Enrollment', back_populates='program_type')

    def __repr__(self):
        return f"<ProgramType {self.name}>"

# Program model
class Program(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    type_id = db.Column(db.Integer, db.ForeignKey('program_types.id'), nullable=False)
    program_type = db.relationship('ProgramType', back_populates='programs')
    enrollments = db.relationship('Enrollment', back_populates='program')

    def __repr__(self):
        return f"<Program {self.title}>"

# Enrollment model
class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    admission_number = db.Column(db.String(50), nullable=False)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    program_type_id = db.Column(db.Integer, db.ForeignKey('program_types.id'), nullable=False)

    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)

    program = db.relationship('Program', back_populates='enrollments')
    program_type = db.relationship('ProgramType', back_populates='enrollments')

    def __repr__(self):
        return f"<Enrollment {self.client_name} | Program: {self.program.title}>"
