# tests/__init__.py

import os
from dotenv import load_dotenv

# Load environment variables from .env in the project root
load_dotenv()

# Optional: Force test config mode
os.environ["FLASK_ENV"] = "testing"
os.environ["TESTING"] = "True"
