from django.shortcuts import render
"""
    This Module defines the views for the 'oc_lettings_site' application.
"""


def index(request):
    """
        View of the main landing page.

        Args:
            request (HttpRequest): The HTTP request.

        Returns:
            HttpResponse: A response object that renders the 'index.html' template.
    """
    return render(request, 'index.html')
