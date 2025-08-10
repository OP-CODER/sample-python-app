import sys
import os
import pytest

# Add your app's folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simple-python-app')))

from app import app  # Import Flask app from app.py

# Optional: Create a pytest fixture for test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Actual test function
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, world!" in response.data
