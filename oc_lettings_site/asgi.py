import os
from django.core.asgi import get_asgi_application

"""
    ASGI configuration for the 'oc_lettings_site' project.
    The `application` object is used by the ASGI server to communicate with the Django project.

    Settings:
        DJANGO_SETTINGS_MODULE (str): The Django settings module to use, set to
            'oc_lettings_site.settings' by default.
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
