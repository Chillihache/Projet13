from django.urls import reverse, resolve
from lettings.views import index, letting

"""
    Tests of urls.py of the 'lettings' application.
"""


def test_lettings_index_url():
    """
        Test that the lettings_index URL resolves to the correct view.
    """
    url = reverse("lettings_index")
    assert resolve(url).func == index


def test_letting_url():
    """
        Test that the letting URL resolves to the correct view.
    """
    url = reverse("letting", kwargs={"letting_id": 1})
    assert resolve(url).func == letting
