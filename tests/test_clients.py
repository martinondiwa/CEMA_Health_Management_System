import unittest
from app import create_app, db
from app.models import Client, Program, Enrollment

class ClientTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create sample client and program
            self.client1 = Client(name="Alice Smith", age=28, gender="Female")
            self.client2 = Client(name="Bob James", age=40, gender="Male")
            self.program = Program(name="Malaria", description="Malaria Treatment")
            db.session.add_all([self.client1, self.client2, self.program])
            db.session.commit()

            # Enroll client1 in the program
            enrollment = Enrollment(client_id=self.client1.id, program_id=self.program.id)
            db.session.add(enrollment)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_view_client_profile_page(self):
        response = self.client.get(f'/profile/{self.client1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alice Smith', response.data)
        self.assertIn(b'Malaria', response.data)

    def test_client_search_found(self):
        response = self.client.post('/search', data={'search': 'Alice'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alice Smith', response.data)

    def test_client_search_not_found(self):
        response = self.client.post('/search', data={'search': 'Nonexistent'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Alice Smith', response.data)
        self.assertIn(b'No clients found', response.data)  # You can customize this in your template

