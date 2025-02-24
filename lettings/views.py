from django.shortcuts import render
from lettings.models import Letting
"""
    This Module defines the views for the 'lettings' application.

    These views fetch data from the database and render it in the respective templates.
"""


def index(request):
    """
        View for the index page that displays every lettings.

        This view retrieves all lettings from the database and displays them on the index page.
        The lettings are passed to the template.

        Args:
            request (HttpRequest): The HTTP request object containing data about the request.

        Returns:
            HttpResponse: A response object that renders the 'index.html' template with the list
                of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/templates/index.html', context)


def letting(request, letting_id):
    """
        View for displaying details of a specific letting.

        This view retrieves a specific letting from the database based on its ID.
        The letting is passed to the template

        Args:
            request (HttpRequest): The HTTP request object containing data about the request.
            letting_id (int): The ID of the letting

        Returns:
            HttpResponse: A response object that renders the 'letting.html' template with the
                details of the requested letting.
        """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
