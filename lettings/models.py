from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
"""
    This module defines the models for the 'lettings' application.
"""


class Address(models.Model):
    """
        Model representing a physical address.

        Attributes:
            number (int): The street number of the address (must be a positive integer, max value
                of 9999).
            street (str): The name of the street (max length of 64 characters).
            city (str): The city where the address is located (max length of 64 characters).
            state (str): The state abbreviation (2 characters long).
            zip_code (int): The zip code of the address (must be a positive integer, max value of
                99999).
            country_iso_code (str): The 3-character ISO code for the country
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
            String representation of the 'Address' model.

            Returns :
                str : A string in the format of 'number street'
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
            Create a custom verbose name for 'Address' model for the django administrator
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
        Model representing a letting property.

        Attributes:
            title (str): The title or name of the letting property (max length of 256 characters).
            address (Address): A OneToOne relationship with the 'Address' model, representing
                the address of the property.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
            String representation of the 'Letting' model.

            Returns :
                str : The title of the letting property.
        """
        return self.title
