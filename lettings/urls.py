"""
URL Configuration for the lettings app.

This module defines URL patterns for the lettings app of the project. The lettings
app is responsible for managing :class:`lettings.Letting` properties and related views.

URL Patterns:
    - ``/lettings/`` - URL for the lettings index page, displaying a list of
      :class:`lettings.Letting` properties.
    - ``/lettings/<int:letting_id>/`` - URL pattern for viewing details of a specific
      :class:`lettings.Letting` property identified by its ID.

Note:
    This file should only include URL patterns specific to the lettings app. Global URL
    patterns and patterns for other apps should be included in the project's main URL
    configuration.

:param path: A module to define URL patterns for Django projects.
"""

from django.urls import path

from lettings import views

app_name = "lettings"

urlpatterns = [
    path("lettings/", views.index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
]
