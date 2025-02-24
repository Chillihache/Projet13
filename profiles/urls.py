from django.urls import path
from profiles.views import index, profile

"""
    This module includes the URL patterns for the 'profiles' application.
    The paths are associated with their respective views defined in the 'profiles.views' module.

    Routes:
        profiles_index: The main page that displays all profiles.
        profile: A page displaying the details of a specific profile based on its username.
"""


urlpatterns = [
    path('', index, name='profiles_index'),
    path('<str:username>/', profile, name='profile'),
]
