from django.contrib import admin
from lettings.models import Address, Letting

"""
    This module allows the registration of
    the "Letting" and "Adress" models with
    the django administrator
"""

admin.site.register(Letting)
admin.site.register(Address)
