import requests
import pytest


@pytest.mark.update
def test_update_profile_name_success(base_url, auth_headers):
    new_name = "NewName"
    response = requests.patch(f"{base_url}/user/name", headers=auth_headers, json={"name": new_name})
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
    assert data["user"]["name"] == new_name, "Имя в ответе не совпадает с новым именем"

@pytest.mark.update
def test_update_profile_name_fail_invalid_headers(base_url):
    new_name = "NewName"
    response = requests.patch(f"{base_url}/user/name", headers={
        "Authorization": f"Bearer 123"
    }, json={"name": new_name})
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}") 

    assert status_code == 401, f"Status-code: {status_code}"
    assert "message" in data, "Нет сообщения об ошибке в ответе"

@pytest.mark.update
def test_update_profile_name_fail_not_headers(base_url):
    new_name = "NewName"
    response = requests.patch(f"{base_url}/user/name", json={"name": new_name})
    data = response.json()
    status_code = response.status_code

    print(f"Status-code: {status_code}")
    print(f"Response: {data}") 

    assert status_code == 401, f"Status-code: {status_code}"
    assert "message" in data, "Нет сообщения об ошибке в ответе"