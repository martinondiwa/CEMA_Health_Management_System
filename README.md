CEMA Health Management System
CEMA Health Management System is a comprehensive web-based application designed to streamline the management of healthcare operations. It is built with a focus on improving doctor-client interactions, managing client data, and facilitating program creation and client enrollments.
Features
•	Doctor/Admin Dashboard: Enables doctors and administrators to manage clients, create programs, and monitor overall system usage.
•	Client Profiles: Allows clients to view their personal health data and track their progress in various health programs.
•	User Authentication: Secure login and registration system for doctors and administrators.
•	Program Management: Ability for doctors to create health programs and enroll clients.
•	RESTful API: Provides an API for interacting with client data programmatically.
Technology Stack
•	Backend: Flask (Python)
•	Frontend: HTML5, CSS3, JavaScript (with Bootstrap and custom styles)
•	Database: SQLAlchemy (for development); can be easily switched to other databases for production (e.g., PostgreSQL, MySQL)
•	Authentication: Flask-Login for user authentication
•	Testing: unittest, pytest
Installation
Prerequisites
•	Python 3.12.3
•	pip (Python package installer)
Steps
1.	Clone the repository:
2.	Set up a virtual environment:
bash
CopyEdit
python3 -m venv venv-Cema #the vittual environment created was name venv-Cema
source venv/bin/activate  

Install dependencies:
bash
CopyEdit
pip install -r requirements.txt
3.	Set up environment variables:
Create a .env file in the root directory with the following content:
plaintext
CopyEdit
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
4.	Run the application:
bash
CopyEdit
python run.py
The app will be available at the local host example ( http://127.0.0.1:5000/.)
Testing
To run tests, make sure the virtual environment is activated, then run:
bash
CopyEdit
pytest tests/
This will execute all unit and integration tests to ensure the application functions correctly.
Contributing
We welcome contributions to improve the CEMA Health Management System. Please follow these guidelines when submitting issues or pull requests:
1.	Fork the repository.
2.	Create a new branch for your feature or bug fix.
3.	Write clear, concise commit messages.
4.	Ensure that tests pass before submitting a pull request.
Contact
For any questions or feedback, feel free to reach out at:
•	Email: suremartin653@gmail.com 
•	GitHub: https://github.com/martinondiwa 

