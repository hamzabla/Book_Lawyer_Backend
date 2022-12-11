import pytest
import json
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
import datetime


@pytest.fixture
def appointments(db):
    return [mixer.blend('appointments.Appointment') for _ in range(3)]


def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


def contains(response, key, value):
    obj = parse(response)
    if key not in obj:
        return False
    return value in obj[key]


def test_customer_anon_user_get_nothing():
    path = reverse('customers-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_customer_user_get_list(appointments):
    path = reverse('customers-list')
    client = get_client(appointments[0].customer)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == 1


def test_customer_retrieve_a_single_appointment(appointments):
    path = reverse('customers-detail', kwargs={'pk': appointments[0].pk})
    client = get_client(appointments[0].customer)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert obj['title'] == appointments[0].title

