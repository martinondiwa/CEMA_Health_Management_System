# CEMA_Health_Management_System main Readme File
CEMA_Health_Management_System/
│
├── app/
│   ├── __init__.py                  # App factory & initialization
│   ├── config.py                    # Configuration classes
│   ├── models.py                    # SQLAlchemy models (Doctor, Client, Program, Enrollment, User)
│   ├── forms.py                     # WTForms for login, registration, etc.
│
│   ├── templates/                   # HTML templates
│   │   ├── base.html                # Shared layout: header, footer, etc.
│   │   ├── home.html                # Public landing page before login
│   │   ├── doctor_dashboard.html    # Main dashboard for doctors/admins
│   │   ├── client_profile.html      # Detailed view of a client
│   │   ├── auth/
│   │   │   ├── login.html           # Login form (doctor/admin)
│   │   │   └── register.html        # Registration form (doctor/admin only)
│
│   ├── static/                      # Static assets
│   │   ├── css/
│   │   │   ├── main.css             # Global styles (base layout, typography)
│   │   │   ├── dashboard.css        # Doctor/admin dashboard styles
│   │   │   ├── forms.css            # Styling for login/register forms
│   │   │   └── client.css           # Styling for client profile/info
│   │   └── js/
│   │       └── main.js              # Optional JS logic
│
│   ├── routes/                      # Flask Blueprints
│   │   ├── __init__.py              # Blueprint registration
│   │   ├── auth_routes.py           # Routes for login, registration (doctors)
│   │   ├── doctor_routes.py         # Dashboard actions: create program, register client, etc.
│   │   ├── client_routes.py         # Profile viewing only
│   │   └── api.py                   # Optional REST API (e.g., fetch client info)
│
├── instance/
│   └── config.py                    # Local config overrides
│
├── tests/                           # Test suite
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_doctor_dashboard.py
│   ├── test_clients.py
│   └── test_api.py
│
├── .env                             # Flask secret keys, DB URI
├── .flaskenv                        # Flask app and environment
├── .gitignore                       # Files/folders to ignore
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
├── run.py                           # Entry script
├── setup.sh                         # Setup script
├── presentation.pptx                # System pitch/design slides
└── prototype_demo.mp4               # System demo recording
