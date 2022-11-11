from rest_framework import status
from rest_framework.test import APIClient
import pytest

endpoint = '/authentication'


def validate_response(response, user):
    response_user = response.data['user']
    assert response_user['username'] == user['username']
    assert response_user['email'] == user['email']
    assert 'token' not in response_user
    assert 'token' in response.data
    assert 'id' in response_user
    assert 'password' not in response_user


@pytest.mark.django_db
def test_login_success(client):
    user = {
        'username': "ahmed_",
        'email': "ahmed@gmail.com",
        'password': "xxx",
        "bio": "I am linguini"
    }

    # register the user
    response = client.post(f'{endpoint}/register/', user)
    assert response.status_code == status.HTTP_201_CREATED

    # login the user
    response = client.post(f'{endpoint}/login/', {'username': "ahmed_", 'password': "xxx", })
    assert response.status_code == status.HTTP_200_OK
    validate_response(response, user)


@pytest.mark.django_db
def test_login_fail(client):
    # login the user
    response = client.post(f'{endpoint}/login/', {'username': "ahmed_osama", 'password': "Passwordxx", })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_logout_success(auth_client):
    client = auth_client()
    response = client.post(f'{endpoint}/logout/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_logout_fail(client):
    response = client.post(f'{endpoint}/logout/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
