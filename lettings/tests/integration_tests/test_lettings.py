import pytest
from django.test import Client
from django.urls import reverse
from lettings.models import Address, Letting

"""
    Test the lettings application.
"""


@pytest.mark.django_db
def test_lettings():
    """
        Test creation and display of lettings
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )

    letting = Letting.objects.create(title="Great Apartment", address=address)

    client = Client()
    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Lettings" in response.content.decode("utf-8")
    assert letting.title in response.content.decode("utf-8")

    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title in response.content.decode("utf-8")
    assert str(letting.address.number) in response.content.decode("utf-8")
    assert letting.address.street in response.content.decode("utf-8")
    assert letting.address.city in response.content.decode("utf-8")
    assert letting.address.state in response.content.decode("utf-8")
    assert str(letting.address.zip_code) in response.content.decode("utf-8")
    assert letting.address.country_iso_code in response.content.decode("utf-8")
