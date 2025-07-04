import requests
import pytest


@pytest.mark.profile
def test_get_profile_success(base_url, auth_headers, user_data):
    response = requests.get(f"{base_url}/user/me", headers=auth_headers)
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}")

    assert status_code == 200, f"Status-code: {status_code}"
    assert "user" in data, "В ответе нет объекта user"
    assert "id" in data["user"], "В объекте user нет поля id"
    assert "email" in data["user"], "В объекте user нет поля email"
    assert "name" in data["user"], "В объекте user нет поля name"
    assert "age" in data["user"], "В объекте user нет поля age"
    assert data["user"]["email"] == user_data["email"], "Email в ответе не совпадает с переданным"

@pytest.mark.profile
def test_get_profile_fail_invalid_headers(base_url):
    response = requests.get(f"{base_url}/user/me", headers={
        "Authorization": f"Bearer 123"
    })
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}")

    assert status_code == 401, f"Status-code: {status_code}"
    assert "message" in data, "Нет сообщения об ошибке в ответе"

@pytest.mark.profile
def test_get_profile_fail_not_headers(base_url):
    response = requests.get(f"{base_url}/user/me")
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}")

    assert status_code == 401, f"Status-code: {status_code}"
    assert "message" in data, "Нет сообщения об ошибке в ответе"

