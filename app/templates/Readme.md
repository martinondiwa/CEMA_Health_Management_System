tes/ folder contains all HTML templates used to render the web pages of the CEMA Health Management System.
Templates are organized to promote a consistent and dynamic user experience across the application.

Structure Overview
base.html
The main layout file. It defines the global page structure, including the header, footer, navigation bar, and links to static assets.
All other templates extend from this base for consistency.

General Pages:

home.html
Public landing page displayed to users before logging in.

doctor_dashboard.html
Dashboard for doctors and administrators, displaying key actions and system metrics.

client_profile.html
Detailed view of an individual client's profile and program enrollment.

create_program.html
Page for doctors/admins to create and configure new health programs.

register_client.html
Form for doctors/admins to register new clients into the system.

search_results.html
Displays results when a search is performed for clients, programs, or users.

Authentication Pages (auth/ folder):

login.html
Login page for doctors and administrators.

register.html
Registration page for creating doctor/admin accounts (restricted access).

Purpose
The templates define the visual and structural layer of the application.
They use Jinja2 templating syntax to dynamically display data passed from Flask routes.

Developer Notes
All templates must extend base.html to maintain design consistency.

Use semantic HTML5 where possible to improve accessibility and SEO.

Keep templates clean by minimizing complex logic in the HTML (move complex operations to views or context processors).

Place all authentication-related templates inside the auth/ folder.

When adding new templates, follow the existing naming convention: use lowercase and underscores (_) for multi-word filenames.


