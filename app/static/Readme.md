tatic/ folder contains all static assets that are served directly to the client without modification.
These files support the visual appearance, layout, and interactivity of the system's web pages.

Structure Overview
css/
Contains stylesheets that define the visual design and layout of the application:

main.css: Global styles, typography, and base layout.

dashboard.css: Styles specific to the doctor/admin dashboard interface.

forms.css: Styling for login, registration, and data entry forms.

client.css: Styling for client profile pages and client-specific views.

js/
Contains optional JavaScript files for dynamic page interactions:

main.js: Manages client-side behaviors such as form validation or interactive elements.

images/
Stores image assets used throughout the application, including logos, profile placeholders, icons, and other visual elements.

Purpose
Static assets enhance the user interface by providing consistent styling, responsive layouts, and improved visual engagement.
They are referenced directly in HTML templates and are not processed dynamically by Flask.

Developer Notes
Keep styles modular: add new CSS files if a major new section is introduced.

Minimize and optimize images for faster page loading times.

Organize images clearly (e.g., images/clients/, images/icons/) if the number of assets grows.

For any new JavaScript functionality, include scripts responsibly at the bottom of the page (before </body>) for better performance.

Always reference static files in templates using Flask’s url_for('static', filename='path/to/file') helper to ensure correct linking.


