from django.apps import AppConfig
"""
    Configuration for the 'lettings' application in the Django project.
"""


class LettingsConfig(AppConfig):
    """
        This class is used to set application-specific settings.

        Attributes:
            default_auto_field (str): The default auto field to use for primary keys.
            name (str): The name of the application, which is 'lettings'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
