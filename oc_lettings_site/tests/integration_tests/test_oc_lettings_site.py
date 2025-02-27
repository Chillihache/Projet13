import pytest
from django.test import Client
from django.urls import reverse

"""
    Test the oc_lettings_site application.
"""


@pytest.mark.django_db
def test_oc_lettings_site():
    """
        Test display of oc_lettings_site.
    """
    client = Client()
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode("utf-8")
