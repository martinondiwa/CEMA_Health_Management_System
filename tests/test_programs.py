import unittest
from app import create_app, db
from app.models import Program, Client, Enrollment

class ProgramTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Creating test programs and clients
            self.program1 = Program(name="HIV", description="HIV Care Program")
            self.program2 = Program(name="TB", description="Tuberculosis Treatment Program")
            self.client1 = Client(name="Alice Smith", age=30, gender="Female")
            db.session.add_all([self.program1, self.program2, self.client1])
            db.session.commit()

            # Enroll client1 in program1
            enrollment = Enrollment(client_id=self.client1.id, program_id=self.program1.id)
            db.session.add(enrollment)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_program(self):
        # Testing that a program can be created and saved
        program = Program.query.filter_by(name="HIV").first()
        self.assertIsNotNone(program)
        self.assertEqual(program.description, "HIV Care Program")

    def test_create_multiple_programs(self):
        # Testing that multiple programs can be created
        program3 = Program(name="Malaria", description="Malaria Treatment Program")
        db.session.add(program3)
        db.session.commit()

        program = Program.query.filter_by(name="Malaria").first()
        self.assertIsNotNone(program)
        self.assertEqual(program.description, "Malaria Treatment Program")

    def test_view_program_details(self):
        # Testing viewing program details (program's clients, etc.)
        response = self.client.get(f'/program/{self.program1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"HIV Care Program", response.data)
        self.assertIn(b"Alice Smith", response.data)  # Client enrolled in the program

    def test_enroll_client_in_program(self):
        # Testing enrolling a client into a new program
        client2 = Client(name="Bob Johnson", age=25, gender="Male")
        program3 = Program(name="TB", description="Tuberculosis Program")
        db.session.add(client2)
        db.session.add(program3)
        db.session.commit()

        # Enrolling client2 in program3
        enrollment = Enrollment(client_id=client2.id, program_id=program3.id)
        db.session.add(enrollment)
        db.session.commit()

        # Verifying the enrollment
        client2 = Client.query.get(client2.id)
        self.assertIn(program3, client2.programs)

    def test_program_not_found(self):
        # Testing trying to view a non-existent program
        response = self.client.get('/program/999')  # Non-existent program ID
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
