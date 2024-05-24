"""
URL Configuration for the core app.

This module defines URL patterns for the core app of the project. The core app
is responsible for handling basic site functionalities such as the homepage.

Patterns defined here include:
    - ``/`` - URL for the homepage, handled by the ``index`` view.
    - ``/sentry-debug/`` - URL for triggering an error, handled by the ``trigger_error`` view.

Note:
    This file should only include URL patterns specific to the core app.
    Global URL patterns and patterns for other apps should be included in
    the project's main URL configuration.

:param path: A module to define URL patterns for Django projects.
"""

from django.urls import path

from core.views import index, trigger_error

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("sentry-debug/", trigger_error, name="trigger_error_sentry"),
]
