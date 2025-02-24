from django.contrib import admin
from profiles.models import Profile

"""
    This module allows the registration of the "Profile" model with the django administrator.
"""

admin.site.register(Profile)
