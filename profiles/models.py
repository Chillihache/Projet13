from django.db import models
from django.contrib.auth.models import User
"""
    This module defines the models for the 'profiles' application.
"""


class Profile(models.Model):
    """
        Model representing a profile.

        Attributes:
            user (User): A OneToOne relationship with the 'User' model.
            favorite_city (str): The favorite city of the user (max length of 64 characters)
        """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
            String representation of the 'Profile' model.

            Returns :
                str : The username of the user linked to the profile.
        """
        return self.user.username
