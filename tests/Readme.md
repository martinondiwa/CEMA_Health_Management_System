ts/ directory contains all unit and integration tests designed to verify the functionality, reliability, and security of the CEMA Health Management System.

Structure
test_auth.py
Tests authentication features, including login, registration, and session management for doctors and admins.

test_doctor_dashboard.py
Tests dashboard functionalities such as program creation, client enrollment, and overall doctor/admin operations.

test_clients.py
Tests client-related workflows including client registration, profile viewing, and search functionalities.

test_api.py
Tests REST API endpoints, validating data retrieval and response structures.

images/
Contains sample image assets used for testing scenarios like file uploads or image processing validations.

Purpose
The test suite ensures that core components of the system behave as expected under various scenarios.
It supports continuous development by detecting regressions early and maintaining system stability as the application evolves.

Testing Standards
Written using unittest and optionally compatible with pytest.

Tests cover both positive (expected workflows) and negative (error handling, edge cases) scenarios.

External dependencies such as databases or file systems are mocked where applicable to maintain test isolation.

Running Tests
Before running tests, ensure all project dependencies are installed and the environment is correctly set up.

To run the entire test suite using pytest:

bash
Copy
Edit
pytest tests/
Alternatively, using Python's built-in unittest discovery:

bash
Copy
Edit
python -m unittest discover -s tests
Developer Notes
Write clear, isolated, and independent test cases.

Maintain high code coverage, especially for critical system components.

Regularly update and expand test cases when new features or major changes are introduced.

Keep test data (such as sample images) lightweight and organized.
