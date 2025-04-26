# tests/test_enrollments.py

import unittest
from app import create_app, db
from app.models import Client, Program, Enrollment

class EnrollmentTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create test clients and programs
            self.client1 = Client(name="John Doe", age=35, gender="Male")
            self.client2 = Client(name="Jane Doe", age=29, gender="Female")
            self.program1 = Program(name="HIV", description="HIV Care Program")
            self.program2 = Program(name="TB", description="Tuberculosis Treatment Program")
            db.session.add_all([self.client1, self.client2, self.program1, self.program2])
            db.session.commit()

            # Enroll client1 in program1 (HIV care)
            enrollment1 = Enrollment(client_id=self.client1.id, program_id=self.program1.id)
            db.session.add(enrollment1)
            db.session.commit()

            # Enroll client2 in both programs
            enrollment2_1 = Enrollment(client_id=self.client2.id, program_id=self.program1.id)
            enrollment2_2 = Enrollment(client_id=self.client2.id, program_id=self.program2.id)
            db.session.add_all([enrollment2_1, enrollment2_2])
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_enroll_client(self):
        # Test that a client has been successfully enrolled into a program
        client = Client.query.get(self.client1.id)
        programs = client.programs
        self.assertEqual(len(programs), 1)  # Should be 1 program (HIV)

    def test_enroll_multiple_programs(self):
        # Test that a client can be enrolled in multiple programs
        client = Client.query.get(self.client2.id)
        programs = client.programs
        self.assertEqual(len(programs), 2)  # Should be 2 programs (HIV, TB)

    def test_enroll_client_view(self):
        # Test enrolling and viewing the client's enrolled programs in the profile
        response = self.client.get(f'/profile/{self.client1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HIV Care Program', response.data)  # Program enrolled in client profile

    def test_enroll_nonexistent_client(self):
        # Test enrolling a non-existent client (should not be possible)
        response = self.client.post('/enroll', data={
            'client_id': 999,  # Non-existent client ID
            'program_id': self.program1.id
        })
        self.assertEqual(response.status_code, 404)  # Expecting a 404 because client does not exist

if __name__ == '__main__':
    unittest.main()
