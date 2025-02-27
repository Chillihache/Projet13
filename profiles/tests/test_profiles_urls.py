from django.urls import reverse, resolve
from profiles.views import index, profile

"""
    Tests of urls.py of the 'profiles' application.
"""


def test_profiles_index_url():
    """
        Test that the profiles_index URL resolves to the correct view.
    """
    url = reverse("profiles_index")
    assert resolve(url).func == index


def test_profile_url():
    """
        Test that the profile URL resolves to the correct view.
    """
    url = reverse("profile", kwargs={"username": "testuser"})
    assert resolve(url).func == profile
