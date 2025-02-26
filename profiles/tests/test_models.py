import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from profiles.models import Profile

"""
    Tests of models.py of the 'profile' application.
"""


@pytest.mark.django_db
def test_profile_creation():
    """
        Test that a profile instance is correctly created
    """
    user = User.objects.create_user(username="testuser", password="testpassword")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    assert profile.user == user
    assert profile.user.username == "testuser"
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_str_method():
    """
        Test the __str__ method of the Profile model.
    """
    user = User.objects.create_user(username="testuser")
    profile = Profile.objects.create(user=user)

    assert str(profile) == "testuser"


@pytest.mark.django_db
def test_profile_favorite_city_blank():
    """
        Test that the favorite_city field can be left blank.
    """
    user = User.objects.create_user(username="testuser")
    profile = Profile.objects.create(user=user)

    assert profile.favorite_city == ""


@pytest.mark.django_db
def test_profile_max_lenght():
    """
        Test that the max_length constraint is enforced for Profile fields
    """
    user = User.objects.create_user(username="testuser")
    profile = Profile(user=user, favorite_city="A" * 65)  # More than max_length=64

    with pytest.raises(ValidationError) as excinfo:
        profile.full_clean()

    errors = excinfo.value.message_dict

    assert "favorite_city" in errors
    assert len(errors) == 1


@pytest.mark.django_db
def test_profile_on_delete_cascade():
    user = User.objects.create_user(username="testuser")
    Profile(user=user)

    user.delete()

    assert Profile.objects.count() == 0
