import pytest
from models.user import User

def test_user_creation():
    """Test that a user is created with the correct attributes."""
    user = User("Eugene", "eugene@example.com")
    assert user.name == "Eugene"
    assert user.email == "eugene@example.com"

def test_user_inheritance():
    """Test that User correctly inherits from Person."""
    user = User("Eugene", "eugene@example.com")
    assert hasattr(user, 'name')

def test_user_to_dict():
    """Test the dictionary conversion for JSON storage."""
    user = User("Eugene", "eugene@example.com")
    user_dict = user.to_dict()
    assert user_dict == {"name": "Eugene", "email": "eugene@example.com"}

def test_user_email_property():
    """Test that the email property is accessible."""
    user = User("Eugene", "eugene@example.com")
    assert user.email == "eugene@example.com"