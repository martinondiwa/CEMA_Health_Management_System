#!/bin/bash

# Print a message to indicate the setup is starting
echo "Setting up the CEMA Health Management System..."

# Step 1: Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv-Cema

# Step 2: Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Step 3: Install required Python dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Step 4: Set up environment variables (optional: if you use .env file)
echo "Setting up environment variables..."
cp .env.example .env  # If you have an example .env file, copy it as .env

# Step 5: Run database migrations (if you use Flask-Migrate)
echo "Running database migrations..."
flask db upgrade

# Step 6: Run tests (optional but recommended)
echo "Running tests to ensure everything is working..."
pytest

# Step 7: Print success message
echo "Setup complete! You can now run the app with 'flask run'."
