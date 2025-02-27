from django.shortcuts import render
from django.http import Http404
from profiles.models import Profile

"""
    This Module defines the views for the 'profiles' application.

    These views fetch data from the database and render it in the respective templates.
"""


def index(request):
    """
        View for the index page that displays every profiles.

        This view retrieves all profiles from the database and displays them on the index page.
        The profiles are passed to the template.

        Args:
            request (HttpRequest): The HTTP request object containing data about the request.

        Returns:
            HttpResponse: A response object that renders the 'index.html' template with the list
                of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/templates/index.html', context)


def profile(request, username):
    """
        View for displaying details of a specific profile.

        This view retrieves a specific profile from the database based on its username.
        The profile is passed to the template.

        Args:
            request (HttpRequest): The HTTP request object containing data about the request.
            username (str): The username of the profile.

        Returns:
            HttpResponse: A response object that renders the 'profile.html' template with the
                details of the requested profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise Http404("Profile not found")
    context = {'profile': profile}
    return render(request, 'profile.html', context)
