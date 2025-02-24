import pytest
from django.contrib.auth.models import User
from profiles.models import Profile

"""
    Tests of models.py of the 'profile' application.
"""


@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username="testuser", password="testpassword")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert profile.user.username == "testuser"
    assert profile.favorite_city == "Paris"
