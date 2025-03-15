from django.urls import reverse, resolve
from django.contrib import admin
from oc_lettings_site.views import index

"""
    Tests of urls.py of the 'oc_lettings_site' application.
"""


def test_index_url():
    """
        Test that the index URL resolves to the correct view.
    """
    url = reverse("index")
    assert resolve(url).func == index


def test_admin_url():
    """
        Test that the admin URL resolves to the correct view
    """
    url = "/inconsspicuous-admin/"
    assert resolve(url).func.__name__ == admin.site.index.__name__
