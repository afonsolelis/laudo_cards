import os
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200  # nosec
    assert "LaudoCards" in response.text  # nosec


def test_read_login():
    response = client.get("/login")
    assert response.status_code == 200  # nosec
    assert "Login" in response.text  # nosec


def test_admin_redirect_unauthorized():
    # Admin page should redirect to login if no session cookie is provided
    response = client.get("/admin", follow_redirects=False)
    assert response.status_code == 303  # nosec
    assert response.headers["location"] == "/login"  # nosec
