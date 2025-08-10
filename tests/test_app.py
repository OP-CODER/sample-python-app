import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simple-python-app')))
from app import app  # assuming `app.py` in the folder holds your Flask app
