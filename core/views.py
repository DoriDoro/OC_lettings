"""
Views for handling requests in the core app.

This module defines views for handling various HTTP requests in the core app.
The views are responsible for rendering templates for the homepage.

Views defined here include:
    - index: Renders the homepage template ('index.html').

Note:
    These views are simple render functions that use Django's 'render' shortcut
    to render templates. They are mapped to specific URLs in the URL configuration
    (urls.py) of the core app.
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Render the homepage.

    This view renders the homepage template ('index.html').

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    return render(request, 'index.html')


def trigger_error(request):
    """
    example for production:
    if request.user.is_authenticated and request.user.is_superuser:
        raise 42
    return HttpResponse(200)
    """
    division_by_zero = 1 / 0
