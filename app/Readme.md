pp Directory - CEMA Health Management System
This app/ folder contains the core functionality of the CEMA Health Management System.
It is organized according to best practices for a scalable and maintainable Flask application.

Structure Overview
__init__.py: Initializes the Flask application and registers Blueprints.

config.py: Defines configuration settings for different environments (development, testing, production).

models.py: Contains SQLAlchemy models for core entities such as Doctor, Client, Program, Enrollment, and User.

forms.py: Defines WTForms classes used for user authentication and data input.

Templates
Located in the templates/ directory.

Includes the base layout (base.html), user interface pages such as home.html, doctor_dashboard.html, and authentication forms under templates/auth/.

Static Assets
Located in the static/ directory.

Organized into css/ and js/ subfolders for styling and optional client-side scripts.

Routes (Blueprints)
Found in the routes/ directory.

Includes modular route handlers for authentication, doctor dashboard activities, client profile views, and API endpoints.

Purpose
The app/ directory defines the main web application structure, separating concerns into models, views, forms, and static files.
It ensures that development is modular, organized, and easy to extend.

Developer Notes
When adding new pages, update the appropriate Blueprint and create corresponding templates and forms as needed.

Follow the existing organization standards for consistency.

Configuration-specific variables should be defined in instance/config.py and not hard-coded.:
