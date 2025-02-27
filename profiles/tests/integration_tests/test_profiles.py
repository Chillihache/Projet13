import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

"""
    Test the profiles application.
"""


@pytest.mark.django_db
def test_profiles():
    """
        Test creation and display of profiles
    """
    user = User.objects.create_user(username="testuser",
                                    first_name="Prenom",
                                    last_name="Nom",
                                    email="prenom.nom@gmail.com")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    client = Client()
    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Profiles" in response.content.decode("utf-8")
    assert profile.user.username in response.content.decode("utf-8")

    url = reverse("profile", kwargs={"username": "testuser"})
    response = client.get(url)

    assert response.status_code == 200
    assert profile.user.username in response.content.decode("utf-8")
    assert profile.user.first_name in response.content.decode("utf-8")
    assert profile.user.last_name in response.content.decode("utf-8")
    assert profile.user.email in response.content.decode("utf-8")
    assert profile.favorite_city in response.content.decode("utf-8")
