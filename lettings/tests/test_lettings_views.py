import pytest
from django.test import RequestFactory
from django.http import Http404
from lettings.models import Address, Letting
from lettings.views import index, letting

"""
    Tests of views.py of the 'lettings' application.
"""


@pytest.mark.django_db
def test_index_view():
    """
        Test that the index view returns the correct response and context (list of settings)
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code="75008",
        country_iso_code="FRA"
    )

    Letting.objects.create(title="Great apartment", address=address)

    request = RequestFactory().get("/")
    response = index(request)

    assert response.status_code == 200
    assert "Lettings" in response.content.decode("utf-8")
    assert "Great apartment" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_index_view_no_lettings():
    """
        Test that the index view returns the correct response without lettings in database
    """
    request = RequestFactory().get("/")
    response = index(request)

    assert response.status_code == 200
    assert "No lettings are available." in response.content.decode("utf-8")


@pytest.mark.django_db
def test_letting_view():
    """
        Test that the letting view returns the correct response and the details of a specific
        letting.
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code="75008",
        country_iso_code="FRA"
    )

    let = Letting.objects.create(title="Great apartment", address=address)

    request = RequestFactory().get(f"/letting/{let.id}/")
    response = letting(request, let.id)

    assert response.status_code == 200
    assert "Great apartment" in response.content.decode("utf-8")
    assert "Avenue des Champs-Élysées" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_letting_view_invalid_letting_id():
    """
        Test that the letting view returns a 404 status code when an invalid letting ID is
        provided.
    """
    request = RequestFactory().get("/letting/1/")

    with pytest.raises(Http404):
        letting(request, 1)
