"""
URL Configuration for the lettings app.

This module defines URL patterns for the lettings app of the project. The lettings
app is responsible for managing letting properties and related views.

Patterns defined here include:
    - /lettings/ - URL for the lettings index page, displaying a list of letting properties.
    - /lettings/<int:letting_id>/ - URL pattern for viewing details of a specific letting
      property identified by its ID.

Note:
    This file should only include URL patterns specific to the lettings app. Global URL
    patterns and patterns for other apps should be included in the project's main URL
    configuration.
"""

from django.urls import path

from lettings import views

app_name = 'lettings'

urlpatterns = [
    path('lettings/', views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
