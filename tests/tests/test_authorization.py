import pytest
import requests
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent 
DATA_DIR = BASE_DIR / "test_data"

with open(DATA_DIR / "valid_users_login.json", encoding="utf-8") as f:
    valid_users_login = json.load(f)

with open(DATA_DIR / "invalid_users_login.json", encoding="utf-8") as f:
    invalid_users_login = json.load(f)

@pytest.mark.authorization
@pytest.mark.parametrize("user", valid_users_login)
def test_authorization_success(base_url, user):
    response = requests.post(f"{base_url}/auth/login", json=user)
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}")

    assert status_code == 200, f"Status-code: {status_code}"
    assert "token" in data, "В ответе нет токена"
    assert "user" in data, "В ответе нет объекта user"
    assert "id" in data["user"], "В объекте user нет поля id"
    assert "email" in data["user"], "В объекте user нет поля email"
    assert "name" in data["user"], "В объекте user нет поля name"
    assert "age" in data["user"], "В объекте user нет поля age"
    assert data["user"]["email"] == user["email"], "Email в ответе не совпадает с переданным"

@pytest.mark.authorization
@pytest.mark.parametrize("user", invalid_users_login)
def test_authorization_fail(base_url, user):
    response = requests.post(f"{base_url}/auth/login", json=user)
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}")

    assert status_code in [422, 500], f"Status-code {status_code}"

    if user["email"] == "" and user["password"] == "":
        assert data["type"] == "validation", f"type: {data['type']}"
        assert data["on"] == "body", f"on: {data['on']}"
        assert "found" in data, "Нет поля found в ответе"
        assert "email" in data["found"], "В объекте found нет поля email"
        assert "password" in data["found"], "В объекте found нет поля password"
    else:
        assert "fields" in data, "Нет сообщения об ошибке в ответе"

