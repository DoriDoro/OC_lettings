"""
Views for handling requests in the core app.

This module defines views for handling various HTTP requests in the core app.
The views are responsible for rendering templates for the homepage, as well as
custom error pages for 404 (Page Not Found) and 500 (Internal Server Error) HTTP errors.

Views defined here include:
    - index: Renders the homepage template ('index.html').
    - error_404: Renders the custom 404 error page template ('404.html') when a
                 Page Not Found error occurs. Accepts an additional 'exception'
                 parameter to capture the exception that triggered the error.
    - error_500: Renders the custom 500 error page template ('500.html') when an
                 Internal Server Error occurs.

Note:
    These views are simple render functions that use Django's 'render' shortcut
    to render templates. They are mapped to specific URLs in the URL configuration
    (urls.py) of the core app.
"""
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


def error_404(request, exception):
    """
    Render the custom 404 error page.

    This view renders the custom 404 error page template ('404.html') when a Page Not
    Found error occurs.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    return render(request, '404.html', status=404)


def error_500(request):
    """
    Render the custom 500 error page.

    This view renders the custom 500 error page template ('500.html') when an Internal
    Server Error occurs.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    return render(request, '500.html', status=500)
