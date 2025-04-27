import unittest
from app import create_app, db
from app.models import Client, Program, Enrollment

class APITestCase(unittest.TestCase):
    def setUp(self):
        # Setup the test app
        self.app = create_app('testing')
        self.client = self.app.test_client()

        # Setup app context and initialize test DB
        with self.app.app_context():
            db.create_all()

            # Create test client and programs
            client1 = Client(name="John Doe", age=30, gender="Male")
            program1 = Program(name="HIV", description="HIV Care Program")
            db.session.add_all([client1, program1])
            db.session.commit()

            # Enroll client in the program
            enrollment = Enrollment(client_id=client1.id, program_id=program1.id)
            db.session.add(enrollment)
            db.session.commit()

            self.test_client_id = client1.id

    def tearDown(self):
        # Drop all tables after each test
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_client_profile_api(self):
        # Make GET request to the client API endpoint
        response = self.client.get(f'/api/client/{self.test_client_id}')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn('client', data)
        self.assertEqual(data['client']['name'], 'John Doe')
        self.assertGreaterEqual(len(data['client']['programs']), 1)

    def test_client_not_found(self):
        response = self.client.get('/api/client/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
