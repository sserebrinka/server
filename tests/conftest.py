import pytest
import requests

BASE_URL = 'http://localhost:3000'

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def user_data():
    return {
        "email": "example_profile@gmail.com",
        "password": "12345",
        "age": 18
    }

@pytest.fixture
def token(user_data, base_url):
    requests.post(f"{base_url}/auth/register", json=user_data)
    response = requests.post(f"{base_url}/auth/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    token = response.json().get("token")
    return token

@pytest.fixture
def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }