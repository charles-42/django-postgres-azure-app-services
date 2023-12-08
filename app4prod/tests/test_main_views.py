from django.test import Client
from django.urls import reverse
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def client():
    return Client()


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)  # Replace with your actual URL path
    assert url == '/'
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_hello_view(client, django_user_model):  # Assuming you have a User model
    # Manually create a user instance
    user = django_user_model.objects.create_user(
        username='testuser', password='password')

    # Simulate a logged-in user
    client.force_login(user)

    # Make a request to the 'hello' view
    url = reverse('hello')
    response = client.get(url)

    # Assert the response status code is 200
    assert response.status_code == 200
    assert url == '/accounts/profile/'
    assert 'hello.html' in [t.name for t in response.templates]
    assert 'username' in response.context
    assert response.context['username'] == 'testuser'
