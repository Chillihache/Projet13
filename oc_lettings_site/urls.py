from django.contrib import admin
from django.urls import path, include
import lettings.urls
import profiles.urls
from oc_lettings_site.views import index

"""
    This module includes the URL patterns for the 'oc_lettings_site' application.

    Routes:
        index: The main landing page of the site.
        admin: The Django administrator interface.
        lettings: Includes the URL patterns for the 'lettings' application.
        profiles: Includes the URL patterns for the 'profiles' application.
"""


urlpatterns = [
    path('inconspicuous-admin/', admin.site.urls),
    path('', index, name='index'),
    path('lettings/', include(lettings.urls)),
    path('profiles/', include(profiles.urls)),
]
