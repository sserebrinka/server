import pytest
import requests
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent 
DATA_DIR = BASE_DIR / "test_data"

with open(DATA_DIR / "users_exist.json", encoding="utf-8") as f:
    users_exist = json.load(f)

with open(DATA_DIR / "users_not_exist.json", encoding="utf-8") as f:
    users_not_exist = json.load(f)

@pytest.mark.exist
@pytest.mark.parametrize("user", users_exist)
def test_exist_success(base_url, user):
    url = f"{base_url}/exist"
    response = requests.post(url, json=user)
    data = response.json()

    assert data['exist'] == True, f"Пользователь с email {user['email']} должен существовать в базе данных"

@pytest.mark.exist
@pytest.mark.parametrize("user", users_not_exist)
def test_exist_fail(base_url, user):
    url = f"{base_url}/exist"
    response = requests.post(url, json=user)
    data = response.json()

    assert data['exist'] == False, f"Пользователь с email {user['email']} не должен существовать в базе данных"