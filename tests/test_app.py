import pytest
from simple_python_app import app  # adjust import based on your app structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage returns a 200 status code and expected content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data or b"Welcome" in response.data  # check for expected text in response
