from rest_framework import status
from rest_framework.test import APIClient
import pytest, zoneinfo

from datetime import datetime

endpoint = '/albums'


def validate_response(response, user):
    response_user = response.data
    assert response_user['name'] == user['name']
    assert response_user['cost'] == user['cost']


@pytest.mark.django_db
def test_create_album(client):
    input_data = {
        'name': "hate",
        "release_date": datetime(2023, 10, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": '123.00',
        "approved": False,
    }

    response = client.post(f'{endpoint}/', input_data)
    assert response.status_code == status.HTTP_201_CREATED

    validate_response(response, input_data)
