"""
Views for handling requests in the core app.

This module defines views for handling various HTTP requests in the core app.
The views are responsible for rendering templates for the homepage.

Views defined here include:
    - index: Renders the homepage template ('index.html').
    - trigger_error: Triggers an event in Sentry.

Note:
    These views are simple render functions that use Django's 'render' shortcut
    to render templates. They are mapped to specific URLs in the URL configuration
    (urls.py) of the core app.

:param render: A module to render templates in Django views.
"""

from django.shortcuts import render


def index(request):
    """
    Render the homepage.

    This view renders the homepage template ('index.html').

    :param HttpRequest request: The HTTP request object.
    :return: Rendered homepage template.
    :rtype: HttpResponse
    """

    return render(request, "index.html")


def trigger_error(request):
    """
    Trigger an error for testing Sentry.

    This view is used for testing purposes to trigger an error in order to
    test Sentry's error tracking functionality.

    :param HttpRequest request: The HTTP request object.
    :return: None
    :rtype: None
    """

    # Example for triggering an error
    division_by_zero = 1 / 0
    return division_by_zero  # This will raise a ZeroDivisionError
