import pytest
from django.test import RequestFactory
from django.http import Http404
from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.views import index, profile

"""
    Tests of views.py of the 'profiles' application.
"""


@pytest.mark.django_db
def test_index_view():
    """
        Test that the index view returns the correct response and context (list of settings)
    """
    user = User.objects.create(username="testuser")
    Profile.objects.create(user=user)

    request = RequestFactory().get("/")
    response = index(request)

    assert response.status_code == 200
    assert "Profiles" in response.content.decode("utf-8")
    assert "testuser" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_index_view_no_profiles():
    """
        Test that the index view returns the correct response without profiles in database
    """
    request = RequestFactory().get("/")
    response = index(request)

    assert response.status_code == 200
    assert "No profiles are available." in response.content.decode("utf-8")


@pytest.mark.django_db
def test_letting_view():
    """
        Test that the profile view returns the correct response and the details of a specific
        profile.
    """
    user = User.objects.create(username="testuser",
                               first_name="Prénom",
                               last_name="Nom",
                               email="prenom.nom@gmail.com")
    pro = Profile.objects.create(user=user, favorite_city="Paris")

    request = RequestFactory().get(f"/profile/{pro.user.username}/")
    response = profile(request, pro.user.username)

    assert response.status_code == 200
    assert "testuser" in response.content.decode("utf-8")
    assert "Prénom" in response.content.decode("utf-8")
    assert "Nom" in response.content.decode("utf-8")
    assert "prenom.nom@gmail.com" in response.content.decode("utf-8")
    assert "Paris" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_profile_view_invalid_profile_username():
    """
        Test that the letting view returns a 404 status code when an invalid letting ID is
        provided.
    """
    request = RequestFactory().get("/letting/InvalidUsername/")

    with pytest.raises(Http404):
        profile(request, "InvalidUsername")
