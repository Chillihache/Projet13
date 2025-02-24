from django.urls import path
from lettings.views import index, letting
"""
    This module includes the URL patterns for the 'lettings' application.
    The paths are associated with their respective views defined in the 'lettings.views' module.

    Routes:
        lettings_index: The main page that displays all lettings.
        letting: A page displaying the details of a specific letting based on its ID.
"""


urlpatterns = [
    path('', index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
