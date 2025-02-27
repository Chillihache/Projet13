from django.test import RequestFactory
from oc_lettings_site.views import index

"""
    Tests of views.py of the 'oc_lettings_site' application.
"""


def test_index_view():
    """
        Test that the index view returns the correct response and context
    """
    request = RequestFactory().get("/")
    response = index(request)

    assert response.status_code == 200
    assert "Holiday Homes" in response.content.decode("utf-8")
