"""
URL Configuration for the core app.

This module defines URL patterns for the core app of the project. The core app
is responsible for handling basic site functionalities such as the homepage.

Patterns defined here include:
    - / - URL for the homepage, handled by the 'index' view.

The 'handler404' and 'handler500' settings are configured to redirect to the
'error_404' and 'error_500' views respectively, which handle custom error pages
for 404 (Page Not Found) and 500 (Internal Server Error) HTTP errors.

Note:
    This file should only include URL patterns specific to the core app.
    Global URL patterns and patterns for other apps should be included in
    the project's main URL configuration.
"""

from django.urls import path

from core.views import index

app_name = 'core'

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

urlpatterns = [
    path('', index, name='index'),
]
