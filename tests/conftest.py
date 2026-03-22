import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provide a TestClient with a fresh app instance for each test"""
    return TestClient(app)


@pytest.fixture
def chess_activity():
    """Sample activity already in the app data"""
    return "Chess Club"


@pytest.fixture
def new_student_email():
    """Email of a student not yet registered"""
    return "newstudent@mergington.edu"


@pytest.fixture
def registered_student_email():
    """Email of a student already registered in Chess Club"""
    return "michael@mergington.edu"
