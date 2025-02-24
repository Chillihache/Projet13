from django.apps import AppConfig
"""
    Configuration for the 'oc_lettings_site' application in the Django project.
"""


class ProfilesConfig(AppConfig):
    """
        This class is used to set application-specific settings.

        Attributes:
            name (str): The name of the application, which is 'profiles'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
